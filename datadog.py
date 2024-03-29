

name: Datadog Vulnerability Analysis with Snyk
description: |-
  Upload the dependency graph to Datadog.
inputs:
  service:
    description: |-
      The service name.
    required: true
  version:
    description: |-
      The version of the application.
    required: true
  site:
    description: |-
      The Datadog site, set to 'datadoghq.com' by default. Needs to be set to 'datadoghq.eu' for Datadog EU users.
    required: false
    default: datadoghq.com

runs:
  using: "composite"
  steps:
  - name: Install Snyk CLI tools
    run: npm install -g snyk
    shell: bash
  - name: Install Datadog-ci
    run: npm install -g --save-dev @datadog/datadog-ci
    shell: bash
  # TODO: Analyse deps.json file to check the content is valid and report errors to the user
  - name: Compress dependency graph
    run: |
      echo "-- Show 10 first lines of deps.json"
      head -n10 deps.json
      echo "-- Remove error message 'Failed to run the process' if present"
      cat deps.json | grep -v "Failed to run the process" > snyk_tmp.json
      mv snyk_tmp.json deps.json
      head -n10 deps.json
      echo "-- Compacting the dependency graph"
      echo "Size of deps.json before compression: `du -sh deps.json | cut -d' ' -f2`"
      cat deps.json | jq -c '.' > snyk_tmp.json
      mv snyk_tmp.json deps.json
      echo "Size of deps.json after compression: `du -sh deps.json | cut -d' ' -f2`"
      echo "-- Remove vulnerability analysis and keep only dependency graph from Snyk output"
      head -n1 deps.json > snyk_tmp.json
      mv snyk_tmp.json deps.json
      echo "Final size of deps.json: `du -sh deps.json | cut -d' ' -f2`"
    shell: bash
  - name: Upload dependency graph
    run: datadog-ci dependencies upload ./deps.json --source snyk --service ${{ inputs.service }} --release-version ${{ inputs.version }}
    shell: bash
    env:
      DATADOG_SITE: ${{ inputs.site }}
