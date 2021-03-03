BiAlert: Serverless, Real-Time & Retroactive Malware Detection
==================================================================

BiAlert is an open-source serverless AWS pipeline where any file uploaded to an S3 bucket is
immediately scanned with a configurable set of `YARA <https://virustotal.github.io/yara/>`_ rules.
An alert will fire as soon as any match is found, giving an incident response team the ability to
quickly contain the threat before it spreads.
