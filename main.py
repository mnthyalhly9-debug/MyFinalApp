name: Build APK
on: [push, pull_request, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install buildozer cython==0.29.33
      - name: Build with Buildozer
        run: buildozer android debug
        env:
          ACCEPT_SDK_LICENSE: "yes"
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: my-app-apk
          path: bin/*.apk
