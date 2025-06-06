---
title: Continuous Integration E2E Test Runs
category: test
---

{% include notification.html message="Out of date. See [ab-install-action](https://github.com/CruGlobal/ab-install-action)" %}

GitHub Actions can be used to automatically run Cypress end to end tests. As an overview we need to:

1. Build a Production version of AppBuilder
2. Bring up the AppBuilder Stack
3. Run the Tests

## Trigger

GitHub allows a number of triggers to be set. These will probably be best in most cases:

```yml
on:
  # Run on any commit to the #master branch
  push:
    branches: [master]
  # Run on pull requests into the #master branch
  pull_request:
    branches: [master]
  # Allows user to trigger the workflow from GitHub's web UI
  workflow_dispatch:
```

## Setup

First, we need to install AppBuilder. A production install is recommended. We can use `npx` so that we don't need to clone ab-cli.

```yml
name: Install AppBuilder
run: npx CruGlobal/ab-cli install ab
```

Next, checkout the current repo into the appropriate directory using [`actions/checkout@v2`](https://github.com/actions/checkout).

## Up

Use AppBuilder's UP.sh script to bring up the stack. Pass in `-t`, to make the stack testable and `-q` to run without the logs. If we don't use `-q` the Workflow will get stuck waiting for UP.sh to finish.

```yml
name: Bring up AppBuilder
run: ./UP.sh -q -t
with:
  working-directory: ./ab
```

## Run Cypress

Use the [Cypress GitHub Action](https://github.com/cypress-io/github-action).
Here are some recommended settings:
with:

```yml
- name: Run Cypress Tests
  uses: cypress-io/github-action@v2
  with:
    working-directory: ./ab
    project: ./test/e2e
    config: baseUrl=http://localhost:8080
    # Wait for the site to be ready
    wait-on: "http://localhost:8080"
    wait-on-timeout: 300
    # We need to set the stack name as an environment variable for
    # the test reset script.
    env: stack=ab
```
