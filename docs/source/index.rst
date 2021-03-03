BiAlert
===========

.. image:: ../images/logo.png
  :align: center
  :scale: 75%
  :alt: BiAlert Logo


BiAlert is a serverless, real-time framework for detecting malicious files. BiAlert can efficiently analyze millions of files a day with a configurable set of `YARA <http://virustotal.github.io/yara/>`_ rules and will trigger an alert as soon as anything malicious is discovered! Organizations can deploy BiAlert to their AWS account in a matter of minutes, allowing them to analyze internal files and documents within the confines of their own environment.


Features
--------

* **Built with Amazon Web Services (AWS):** An AWS account is all you need to deploy BiAlert.
* **Broad YARA support:** BiAlert includes dozens of YARA rules out-of-the-box and makes it easy to add your own rules or clone them from other repositories.
* **Real-Time:** Files uploaded to BiAlert (S3 bucket) are immediately queued for analysis.
* **Serverless:** All computation is handled by `Lambda <https://aws.amazon.com/lambda/>`_ functions. No servers to manage means stronger security and automatic scaling!
* **Infrastructure-As-Code:** The entire infrastructure is described with `Terraform <https://www.terraform.io/>`_ configuration files, enabling anyone to deploy BiAlert in a matter of minutes with a single command.
* **Retroactive Analysis:** After updating the YARA ruleset, BiAlert can retroactively scan the entire file corpus to find any new matches.
* **Production-Ready:** BiAlert ships with a custom metric dashboard and alarms which automatically trigger on error conditions.
* **Low Cost:** The AWS bill is based only on how many files you upload and how often they are re-analyzed.


Resources
---------

* `GitHub Repo <https://github.com/tho-asterist/BiAlert>`_
* `Blog Post <https://medium.com/tho-asterist-engineering/BiAlert-real-time-serverless-malware-detection-ca44370c1b90>`_
* `Slack <https://BiAlert.herokuapp.com/>`_ (unofficial)


Table of Contents
=================
.. toctree::
   :maxdepth: 3

   getting-started
   iam-group
   architecture
   adding-yara-rules
   deploying
   analyzing-files
   yara-matches
   metrics-and-monitoring
   troubleshooting-faq
   credits
