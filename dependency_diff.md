# Dependency Diff

The table below documents the audited update path from the previous (pre-upgrade) versions to the secure, Python 3.10+ compatible releases now defined in `requirements.txt`.

| Library | Before | After | Notes |
| --- | --- | --- | --- |
| numpy | 1.16.4 | 1.26.4 | Latest minor release, better performance, maintained security fixes, and compatible with pandas 2.x |
| pandas | 0.24.2 | 2.1.4 | Replaced deprecated APIs, includes numerous security patches, supports Python 3.8+ |
| scipy | 1.2.1 | 1.11.3 | Updated to match modern numpy, resolves CVEs and adds improved linear algebra performance |
| requests | 2.20.0 | 2.32.0 | Includes TLS/SSL fixes and removes vulnerable dependency on urllib3 1.24 |
| PyYAML | 3.13 | 6.0 | Secured against deserialization exploits; Python 3.10+ compatible |
| matplotlib | 2.2.3 | 3.8.1 | Matches newer backend APIs, fixes DPI/agg issues, modern security hardening |
| Pillow | 5.4.1 | 12.0.0 | Numerous image-handling CVE resolutions and support for current Python versions |
