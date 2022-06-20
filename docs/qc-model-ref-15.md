# Template for Quality Models

Reviewer: CL

Reference:  (ID = 152) - EOSC-synergy: A set of Common Service Quality Assurance Baseline Criteria for Research Projects, Pablo Orviz, et al. https://digital.csic.es/handle/10261/214441

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Category | Comment |
| :------: | :---: | :--------: | :-----------------: | :------: | :-----: |
|SvcQC.Api01 |Validation of features |API testing MUST cover the validation of the features outlined in the specification (aka contract testing). |Manaul |API Testing | |
|SvcQC.Api01.1 |Compliant with OpenAPI Specification (OAS)  |Any change in the API not compliant with the OAS MUST NOT pass contract testing. |Manual |API Testing | |
|SvcQC.Api01.2 |Use of OAS |The use of OAS SHOULD narrow down the applicable set of test cases to the features described in the specification, avoiding unnecessary assertions. |Manual |API Testing | |
|SvcQC.Api02 |Security-related assessment |API testing MUST include the assessment of the security-related criteria. | Manual |API Testing | |
|SvcQC.Api03 |Use of test doubles |API testing SHOULD involve the use of test doubles, such as mock servers or stubs, that act as a validation layer for the incoming requests. |Automatic/Manual |API Testing | |
|SvcQC.Int01 |New functionality |Whenever a new functionality is involved, integration testing MUST guarantee the operation of any previously-working interaction with external Services [SQA-QC.Int01]. When using APIs, contract testing MUST detect any disruption in the communication between provider and consumer endpoints, through the validation of the API specification [SvcQC.Api01]. |Manual/Automatic |Integration Testing | |
|SvcQC.Int02 |Automation |Integration testing SHOULD be automated. |Automatic |Integration Testing | |
|SvcQC.Int03 |Pilot/Testbeds |Ad-hoc pilot Service infrastructures and/or local testbeds MAY be used to cope with the integration testing requirements. |Manual/Automatic |Integration Testing | |
|SvcQC.Fun01 |Full scope |Functional testing SHOULD tend to cover the full scope -e.g. positive, negative, edge cases- for the set of functionality that the Service claims to provide. | Manual/Automatic |Functional Tests | |
|SvcQC.Fun01.1 |Featuure disruptions |When using APIs, contract testing MUST detect any disruption in the features exposed by the provider to the consumer, through the validation of the API specification. |Automatic/Manual |Functional Tests | |
|SvcQC.Fun01.2 |Web interface |Functional tests SHOULD include the Web interface of the Service. |Automatic/Manual |Functional Tests | |
|SvcQC.Fun02 |Automatic checks |Functional tests SHOULD be checked automatically. |Automatic |Functional Tests | |
|SvcQC.Fun03 |Tests provided by developers |Functional tests SHOULD be provided by the developers of the underlying software. |Manual |Functional Tests | |
|SvcQC.Per01 |Varying loads  |Performance testing SHOULD be carried out to check the Service performance under varying loads. |Automatic |Performance Tests | |
|SvcQC.Per02 |Stress testing |Stress testing SHOULD be carried out to check the Service to determine the behavioral limits under sudden increased load. |Automatic |Performance Tests | |
|SvcQC.Per03 |Scalability testing |Scalability testing MAY be carried out to check the Service ability to scale up and/or scale out when its load reaches the limits. |Automatic/Manual |Performance Tests | |
|SvcQC.Per04 |Elasticity testing |Elasticity testing MAY be carried out to check the Service ability to scale out or scale in, depending on its demand or workload. |Automatic/Manual |Performance Tests | |
|SvcQC.Doc01 |Online  |Documentation MUST be available online, easily findable and accessible. |Automatic |Documentation | |
|SvcQC.Doc02 |PID |Documentation SHOULD have a Persistent Identifier (PID). |Automatic  |Documentation | |
|SvcQC.Doc03 |Version controlled |Documentation MUST be version controlled. |Automatic  |Documentation | |
|SvcQC.Doc04 |Updates |Documentation MUST be updated on new Service versions involving any change in the installation, configuration or behaviour of the Service. |Manual  |Documentation | |
|SvcQC.Doc05 |Inaccuracy and Unclear Documentation |Documentation MUST be updated whenever reported as inaccurate or unclear. |Manual |Documentation | |
|SvcQC.Doc06 |License |Documentation MUST have a non-software license. |Manual |Documentation | |
|SvcQC.Doc07 |Target Audience |Documentation MUST be produced according to the target audience, varying according to the Service specification. |Manual |Documentation | |
|SvcQC.Doc07.2 |Deployment and Administration |The identified types of documentation and their RECOMMENDED content are Installation and configuration guides, and Service Reference Card with the following RECOMMENDED content: Brief functional description, List of proceses and daemons, init scripts and options, List of configuration files, locatin and example or template, Log files location and other useful audit information, List of ports, Service state informatio, List of cron jobs, Security information, FAQs and troubleshooting. |Manual |Documentation | |
|SvcQC.Doc07.3 |User |Detailed User Guide for the Serice. Public API documentation (if applicable). Command-line (CLI) reference (if applicable) |Manual |Documentation | |
|SvcQC.Sec01 |Service public endpoints and APIs |The Service public endpoints and APIs MUST be secured with data encryption. |Automatic |Security | |
|SvcQC.Sec01.1 |Service ciphers |The Service MUST use strong ciphers for data encryption. |Automatic |Security | |
|SvcQC.Sec02 |Service authentication |The Service SHOULD have an authentication mechanism. |Automatic |Security | |
|SvcQC.Sec02.1 |Service composition and authentication |Whenever dealing with a Service Composition, such as microservice architectures, the Services SHOULD be managed by a centralized authentication mechanism. |Automatic |Security | |
|SvcQC.Sec02.2 |Service API gateway | In publicly-accessible APIs, Service authentication SHOULD be handled through an API gateway in order to control the traffic and protect the backend services from overuse. |Automatic |Security | |
|SvcQC.Sec03 |Service authorization |The Service SHOULD implement an authorization mechanism. |Automatic |Security | |
|SvcQC.Sec03.1 |Service composition and authorization |In Service Composition environments, the authorization mechanism SHOULD uniquely grant the essential access permissions for each Service according to the principle of least privilege (PoLP). |Automatic |Security | |
|SvcQC.Sec04 |Service Credential and Signatures |The Service MUST validate the credentials and signatures. |Automatic |Security | |
|SvcQC.Sec04.1 |Service credential and certification authority |Credentials used in the Service MUST be signed by a recognized and trusted
certification authority. |Automatic |Security | |
|SvcQC.Sec05 |Service data regulations |The Service MUST handle personal data in compliance with the applicable regulations, such as the General Data Protection Regulation (GDPR) within the European boundaries. |Automatic |Security | |
|SvcQC.Sec06 |Service black-box testing |The Service SHOULD be audited in accordance with the black-box testing criteria identified by de-facto (cyber)security standards and good practices. |Automatic |Security | |
|SvcQC.Sec06.1 |Dynamic Application Secuirty Testing (DAST) |DAST checks MUST be executed, through the use of ad-hoc tools, directly to an operational Service in order to uncover runtime security vulnerabilities and any other environment-related issues (e.g. SQL injection, cross-site scripting or DDOS). The latest release of OWASP's Web Security Testing Guide and the NIST's Technical Guide to Information Security Testing and Assessment MUST be considered for carrying out comprehensive Service security testing. |Manual |Security | |
|SvcQC.Sec06.2 |Black-box pentration testing | Penetration testing (manual or automated) MAY be part of the application security verification effort.|Automatic/Manual |Security | |
|SvcQC.Sec06.3 |Security assessment  |The security assessment of the target system configuration is particularly important to reduce the risk of security attacks. The benchmarks delivered by the Center for Internet Security (CIS)  and the NIST's Security Assurance Requirements for Linux Application Container Deployments MUST be considered for this task. |Manual |Security | |
|SvcQC.Sec07 |IaC Testing |IaC testing, from [SvcQC.Aud02] criterion, MUST cover the security auditing of the IaC templates (SaC) in order to assure the deployment of secured Services. For all the third-party dependencies used in the IaC templates (including all kind of software artefacts, such as Linux packages or container-based images): |Manual  |Security | |
|SvcQC.Sec07.1 |Vulnerability scanning |SaC MUST perform vulnerability scanning of the artefact versions in use. |Automatic |Security | |
|SvcQC.Sec07.2 |Trust and Signature |SaC SHOULD verify that the artefacts are trusted and digitally signed. |Automatic |Security | |
|SvcQC.Sec07.3 |Security policy scans |SaC MUST scan IaC templates to uncover misalignments with widely-accepted security policies from [SvcQC.Sec06] criteria, such as non-encrypted secrets or disabled audit logs. |Automatic |Security | |
|SvcQC.Sec07.4 |Security requirement violations |SaC MAY be used to seek, in the IaC templates, for violations of security requirements outlined in the applicable regulations from criterion [SvcQC.Sec05]. |Manual |Security | |
|SvcQC.Pol1.1 |Acceptable Usage Policy |Acceptable Usage Policy (AUP): Is a set of rules applied by the owner, creator or administrator of a network, Service or system, that restrict the ways in which the network, Service or system may be used and sets guidelines as to how it should be used. The AUP can also be referred to as: Acceptable Use Policy or Fair Use Policy. |Automatic |Policies | |
|SvcQC.Pol1.2 |Access Policy and Terms of Use |Access Policy or Terms of Use: represent a binding legal contract between the users (and/or customers), and the Provider of the Service. The Access Policy mandates the users (and/or customers) access to and the use of the Provider's Service. |Automatic |Policies | |
|SvcQC.Pol1.3 |Privacy policy |Privacy Policy: Data privacy statement informing the users (and/or customers), about which personal data is collected and processed when they use and interact with the Service. It states which rights the users (and/or customers) have regarding the processing of their data. |Automatic |Policies | |
|SvcQC.Sup01 |Service Tracker/Helpdesk |The Service MUST have a tracker or helpdesk for operational and users issues. |Automatic/Manual |Support | |
|SvcQC.Sup02 |Service Issue Tracker  |The Service SHOULD have a tracker for the underlying software issues. |Manual |Support | |
|SvcQC.Sup03 |Operational Level Agreement (OLA) |The Service SHOULD include an Operational Level Agreement (OLA) with the
infrastructure where it is integrated. |Automatic |Support | |
|SvcQC.Sup04 |Service Level Agreement (SLA) |The Service MAY include Service Level Agreement (SLA) with user communities. |Automatic |Support | |
|SvcQC.Aud01 |IaC Templates |A production-ready Service SHOULD be deployed as a workable system with the minimal user or system administrator interaction leveraging IaC templates. |Automatic |Automated Deployment (Repeatability and Reliability) | |
|SvcQC.Aud02 |Immutable Infrastructures |Any future change to a deployed Service SHOULD be done in the form of a new deployment, in order to preserve immutable infrastructures. |Automatic  |Automated Deployment (Repeatability and Reliability) | |
|SvcQC.Aud03 |Specific testing frameworks |IaC SHOULD be validated by specific (unit) testing frameworks for every change being done. |Automatic  |Automated Deployment (Repeatability and Reliability)  | |
|SvcQC.Aud03.1 | Idempotent tests |IaC (unit) tests MUST be idempotent. |Automatic |Automated Deployment (Repeatability and Reliability) | |
|SvcQC.Mon01 |Operational Production State |The Service in an operational production state SHOULD be monitored for functional-related criteria. |Automatic |Monitoring | |
|SvcQC.Mon01.1 |Service Public endpoints |The Service public endpoints MUST be monitored. |Automatic |Monitoring | |
|SvcQC.Mon01.2 |Service public APIs |The Service public APIs MUST be monitored. Use functional tests of criteria [SvcQC.Fun01.2]. |Automatic |Monitoring | |
|SvcQC.Mon01.3 |Service Web Interface |The Service Web interface MAY be monitored. Use functional tests of criteria [SvcQC.Fun01.3]. |Automatic |Monitoring | |
|SvcQC.Mon02 |Security |The Service MUST be monitored for security-related criteria. |Automatic |Monitoring | |
|SvcQC.Mon02.1 |Public endpoints and APIs |The Service MUST be monitored for public endpoints and APIs secured and strong ciphers for encryption. Use Security tests of criteria [SvcQC.Sec02] and [SvcQC.Sec05]. |Automatic |Monitoring | |
|SvcQC.Mon02.2 |DAST |The Service SHOULD be monitored with DAST checks. Use Security tests of criteria [SvcQC.Sec06]. |Automatic |Monitoring | |
|SvcQC.Mon03 |Infrastructure |The Service MUST be monitored for infrastructure-related criteria. |Automatic |Monitoring | |
|SvcQC.Mon03.1 |Unit tests |IaC (unit) tests [SvcQC.Aud02] SHOULD be reused as monitoring tests, thus avoiding duplication. |Automatic |Monitoring | |
|SvcQC.Met01 |Metrics |The Service SHOULD implement the collection of metrics. |Manual/Automatic |Metrics | |
|SvcQC.Met01.1 |Cumulative metrics |The collection of metrics SHOULD be cumulative over time and timestamped, so that the values can be queried per time interval. | Automatic|Metrics | |
|SvcQC.Met01.2 |Registered users |The metric Number of registered users SHOULD be collected. |Automatic |Metrics | |
|SvcQC.Met01.3 |Active users |The metric Number of active users over a given period of time MAY be collected. |Automatic |Metrics | |
|SvcQC.Met01.4 |Computing resources |The metric Amount of computing resources per user or per group MAY be collected. The metric unit depends on the type of service and infrastructure. An example is CPU x hours. |Automatic |Metrics | |
|SvcQC.Met01.5 |Storage resources |The metric Amount of storage resources per user or per group MAY be collected. The metric unit depends on the type of service and infrastructure. An example is GByte x hours. |Automatic |Metrics | |


* Codename: the quality metric may have a codename when defining the model (when available))
* Name: name of the quality metric
* Definition: definition of the quality metric
* Automate/Manual: if the metric maybe automated or only evaluated manually (or through interview)
* Comment: if the criteria/metric is deemed appropriate for our document, or if it is subjective
  and difficult to measure.

## Category

* API Testing
* Integration Testing
* Functional Tests
* Performance Tests
* Documentation
* Security
* Policies
* Support
* Automated Deployment
* Monitoring
* Metrics

