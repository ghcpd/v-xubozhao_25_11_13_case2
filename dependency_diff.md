# Dependency Version Diff Report

This report lists the dependency upgrades from the original `requirements.txt` to the updated versions in this workspace. It highlights obsolescence, compatibility, and security considerations.

| Library | Original Version | Updated Version | Notes |
|--------:|:----------------:|:---------------:|:------|
| numpy | 1.16.4 | 2.3.4 | Major improvements and performance; 2.x is maintained and compatible with Python 3.10+. Large API changes are rare but test code that relied on legacy behavior. |
| pandas | 0.24.2 | 2.3.3 | The 0.24.x series is EOL and has multiple breaking changes compared to 2.x; migrating from 0.x to 2.x may require code changes, especially for deprecated APIs. |
| scipy | 1.2.1 | 1.16.3 | Latest SciPy release with many bugfixes and optimizations; ensures compatibility with modern NumPy versions. |
| requests | 2.20.0 | 2.32.5 | Requests 2.20 contains vulnerabilities patched in later releases; upgrade recommended for TLS fixes and security patches. |
| PyYAML | 3.13 | 6.0.3 | PyYAML 3.x is known for insecure load() usage vulnerabilities; upgrade to 6.x and use `yaml.safe_load` instead of `yaml.load`. |
| matplotlib | 2.2.3 | 3.10.7 | Matplotlib 2.x is obsolete and incompatible with modern style; 3.x includes many backend and API changes - use Agg backend for headless systems. |
| Pillow | 5.4.1 | 12.0.0 | Pillow 5.x is outdated and has performance and security corrections in later releases; upgrade recommended for better format support and fixes. |

> Notes:
> - Tests may require code updates when upgrading from 0.x or 1.x series to 2.x (pandas/numpy/scipy). Run unit/integration tests to detect regressions after upgrades.
> - `yaml.safe_load` should be used to avoid arbitrary code execution when parsing untrusted YAML input.
> - Consider pinning to smaller ranges like `numpy>=1.25,<2.0` if you want to avoid jumping to 2.x major version in production.

This file was auto-generated to document upgrade choices; adjust per your deployment constraints and test outcomes.

## Additional Notes
- If you run into dependency conflicts (e.g., `azureml-dataprep`/`azureml` pinning NumPy <1.24 on Windows), consider creating a virtual environment dedicated to this project or pin a lower NumPy (e.g., `numpy~=1.23`) and test whether your code still runs.
- Major version jumps (0.x/1.x -> 2.x) may require code changes; keep unit tests handy and run them before deployment.
