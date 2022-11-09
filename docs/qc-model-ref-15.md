# QM Reference 15: (paper ID = 152)

Reviewer: CL (Cerlane Leong)

Reference:  (ID = 152) - EOSC-synergy: A set of Common Service Quality Assurance Baseline Criteria for Research Projects, Pablo Orviz, et al.
<https://digital.csic.es/handle/10261/214441>

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Characteristics | Comment |
| :------: | :---: | :--------: | :-----------------: | :-------------: | :-----: |
| SvcQC.Dep01 | Deployment production-ready Service | A production-ready Service SHOULD be deployed as a workable system with
  the minimal user or system administrator interaction leveraging IaC templates. | Aut | Installability | |
| SvcQC.Dep02 | Preserve immutable infrastructures | Any future change to a deployed Service SHOULD be done in the form of a
  new deployment, in order to preserve immutable infrastructures. | Aut | Installability | |
| SvcQC.Dep03 | IaC validation on changes | IaC SHOULD be validated by specific (unit) testing frameworks for every
  change being done. | Aut | Installability | |
| SvcQC.Api01 | Validation of features | API testing MUST cover the validation of the features outlined in the specification (aka contract testing). | Aut | Functional suitability | |
| SvcQC.Api01.1 | Compliant with OpenAPI Specification (OAS)  | Any change in the API not compliant with the OAS MUST NOT pass contract testing. | Aut | Functional suitability | |
| SvcQC.Api01.2 | Use of OAS | The use of OAS SHOULD narrow down the applicable set of test cases to the features described in the specification, avoiding unnecessary assertions. | Aut | Functional suitability | |
| SvcQC.Api02 | Security-related assessment | API testing MUST include the assessment of the security-related criteria. | Aut | Functional suitability | |
| SvcQC.Api03 | Use of test doubles | API testing SHOULD involve the use of test doubles, such as mock servers or stubs, that act as a validation layer for the incoming requests. | Aut | Functional suitability | |
| SvcQC.Int01 | Integration testing | Whenever a new functionality is involved, integration testing MUST guarantee the operation of any previously-working interaction with external Services | Aut | Functional suitability | |
| SvcQC.Int02 | Integration testing, avoid non operational services | Integration testing MUST NOT rely on non-operational or out-of-the-warranty
  services. | Aut | Functional suitability | |
| SvcQC.Int03 | Integration testing use pilot/Testbeds |Ad-hoc pilot Service infrastructures and/or local testbeds MAY be used to cope with the integration testing requirements. | Aut | Functional suitability | |
| SvcQC.Int04 | Integration testing automation | Integration testing SHOULD be automated. | Aut | Functional suitability | |
| SvcQC.Fun01 | Functional testing, full scope | Functional testing SHOULD tend to cover the full scope -e.g. positive, negative, edge cases- for the set of functionality that the Service claims to provide. | Aut | Functional suitability | |
| SvcQC.Fun01.1 | Functional testing, detect feature disruptions | When using APIs, contract testing MUST detect any disruption in the features exposed by the provider to the consumer, through the validation of the API specification. | Aut | Functional suitability | |
| SvcQC.Fun01.2 | Functional testing, Web interface | Functional tests SHOULD include the Web interface of the Service. | Aut | Functional suitability | |
| SvcQC.Fun02 | Functional testing, Automation | Functional tests SHOULD be checked automatically. | Aut | Functional suitability | |
| SvcQC.Fun03 | Functional testing, Tests provided by developers | Functional tests SHOULD be provided by the developers of the underlying software. | Aut | Functional suitability | |
| SvcQC.Per01 | Performance testing | Performance testing SHOULD be carried out to check the Service performance under varying loads. | Aut | Functional suitability | |
| SvcQC.Per02 | Stress testing | Stress testing SHOULD be carried out to check the Service to determine the behavioral limits under sudden increased load. | Aut | Functional suitability | |
| SvcQC.Per03 | Scalability testing | Scalability testing MAY be carried out to check the Service ability to scale up and/or scale out when its load reaches the limits. | Aut | Functional suitability | |
| SvcQC.Per04 | Elasticity testing | Elasticity testing MAY be carried out to check the Service ability to scale out or scale in, depending on its demand or workload. | Aut | Functional suitability | |
| SvcQC.Sec01 | Public endpoints and APIs encrypted | The Service public endpoints and APIs MUST be secured with data encryption. | Aut |Security | |
| SvcQC.Sec01.1 | Strong ciphers | The Service MUST use strong ciphers for data encryption. | Aut | Security | |
| SvcQC.Sec02 | Service authentication | The Service SHOULD have an authentication mechanism. | Aut | Security | |
| SvcQC.Sec02.1 | Service composition centralized authentication | Whenever dealing with a Service Composition, such as microservice architectures, the Services SHOULD be managed by a centralized authentication mechanism. | Aut | Security | |
| SvcQC.Sec02.2 | Protect the backend services API gateway | In publicly-accessible APIs, Service authentication SHOULD be handled through an API gateway in order to control the traffic and protect the backend services from overuse. | Aut | Security | |
| SvcQC.Sec03 | Service composition centralized authorization | The Service SHOULD implement an authorization mechanism. | Aut | Security | |
| SvcQC.Sec03.1 | Service composition authorization access permissions | In Service Composition environments, the authorization mechanism SHOULD uniquely grant the essential access permissions for each Service according to the principle of least privilege (PoLP). | Aut |Security | |
| SvcQC.Sec04 | Service Credential and Signatures validation | The Service MUST validate the credentials and signatures. | Aut | Security | |
| SvcQC.Sec04.1 | Service credential and certification trusted authority | Credentials used in the Service MUST be signed by a recognized and trusted certification authority. | Aut | Security | |
| SvcQC.Sec05 | Service compliance with data regulations (GDPR) | The Service MUST handle personal data in compliance with the applicable regulations, such as the General Data Protection Regulation (GDPR) within the European boundaries. | Aut | Security | |
| SvcQC.Sec06 | Service black-box security testing | The Service SHOULD be audited in accordance with the black-box testing criteria identified by de-facto (cyber)security standards and good practices. | Aut | Security | |
| SvcQC.Sec06.1 | Dynamic Application Security Testing (DAST) | DAST checks MUST be executed, through the use of ad-hoc tools, directly to an operational Service in order to uncover runtime security vulnerabilities and any other environment-related issues (e.g. SQL injection, cross-site scripting or DDOS). The latest release of OWASP's Web Security Testing Guide and the NIST's Technical Guide to Information Security Testing and Assessment MUST be considered for carrying out comprehensive Service security testing. | Aut | Security | |
| SvcQC.Sec06.2 | Interactive Application Security Testing (IAST) | Interactive Application Security Testing (IAST), analyzes code for security vulnerabilities while the app is run by an automated test. IAST **SHOULD** be performed to a service in an operating state. | Aut | Security | |
| SvcQC.Sec06.3 | Security Black-box penetration testing | Penetration testing (manual or automated) MAY be part of the application security verification effort.| Aut |Security | |
| SvcQC.Sec06.4 | Security assessment  | The security assessment of the target system configuration is particularly important to reduce the risk of security attacks. The benchmarks delivered by the Center for Internet Security (CIS)  and the NIST's Security Assurance Requirements for Linux Application Container Deployments MUST be considered for this task. | Aut | Security | |
| SvcQC.Sec07 | Security as Code (SaC) Testing | IaC testing, from [SvcQC.Aud02] criterion, MUST cover the security auditing of the IaC templates (SaC) in order to assure the deployment of secured Services. For all the third-party dependencies used in the IaC templates (including all kind of software artefacts, such as Linux packages or container-based images): | Aut | Security | |
| SvcQC.Sec07.1 | SaC Vulnerability scanning | SaC MUST perform vulnerability scanning of the artefact versions in use. | Aut | Security | |
| SvcQC.Sec07.2 | SaC Trust and Signature | SaC SHOULD verify that the artefacts are trusted and digitally signed. | Aut | Security | |
| SvcQC.Sec07.3 | SaC Security policy scans | SaC MUST scan IaC templates to uncover misalignments with widely-accepted security policies, such as non-encrypted secrets or disabled audit logs. | Aut | Security | |
| SvcQC.Sec07.4 | SaC Security requirement violations | SaC MAY be used to seek, in the IaC templates, for violations of security requirements outlined in the applicable regulations. | Aut | Security | |
| SvcQC.Doc01 | Documentation Online | Documentation MUST be available online, easily findable and accessible. | Aut | Supportability | |
| SvcQC.Doc02 | Documentation PID | Documentation SHOULD have a Persistent Identifier (PID). | Aut  | Supportability | |
| SvcQC.Doc03 | Documentation Version controlled | Documentation MUST be version controlled. | Aut  | Supportability | |
| SvcQC.Doc04 | Documentation Updates | Documentation MUST be updated on new Service versions involving any change in the installation, configuration or behaviour of the Service. | Man  | Supportability | |
| SvcQC.Doc05 | Documentation Inaccuracy and Unclear | Documentation MUST be updated whenever reported as inaccurate or unclear. | Man | Supportability | |
| SvcQC.Doc06 | Documentation License | Documentation MUST have a non-software license. | Aut | Supportability | |
| SvcQC.Doc07 | Documentation Target Audience | Documentation MUST be produced according to the target audience, varying according to the Service specification. | Man | Supportability | |
| SvcQC.Doc07.1 | Documentation Deployment and Administration | The identified types of documentation and their RECOMMENDED content are Installation and configuration guides, and Service Reference Card with the following RECOMMENDED content: Brief functional description, List of proceses and daemons, init scripts and options, List of configuration files, locatin and example or template, Log files location and other useful audit information, List of ports, Service state informatio, List of cron jobs, Security information, FAQs and troubleshooting. | Man | Supportability | |
| SvcQC.Doc07.2 | Documentation User | Detailed User Guide for the Serice. Public API documentation (if applicable). Command-line (CLI) reference (if applicable) | Man | Supportability | |
| SvcQC.Pol1.1 | Acceptable Usage Policy | Acceptable Usage Policy (AUP): Is a set of rules applied by the owner, creator or administrator of a network, Service or system, that restrict the ways in which the network, Service or system may be used and sets guidelines as to how it should be used. The AUP can also be referred to as: Acceptable Use Policy or Fair Use Policy. | Aut | Supportability | |
| SvcQC.Pol1.2 | Access Policy and Terms of Use | Access Policy or Terms of Use: represent a binding legal contract between the users (and/or customers), and the Provider of the Service. The Access Policy mandates the users (and/or customers) access to and the use of the Provider's Service. | Aut | Supportability | |
| SvcQC.Pol1.3 | Privacy policy | Privacy Policy: Data privacy statement informing the users (and/or customers), about which personal data is collected and processed when they use and interact with the Service. It states which rights the users (and/or customers) have regarding the processing of their data. | Aut | Supportability | |
| SvcQC.Sup01 | Service Tracker/Helpdesk | The Service MUST have a tracker or helpdesk for operational and users issues. | Man | Supportability | |
| SvcQC.Sup02 | Service Issue Tracker  | The Service SHOULD have a tracker for the underlying software issues. | Man | Supportability | |
| SvcQC.Sup03 | Operational Level Agreement (OLA) | The Service SHOULD include an Operational Level Agreement (OLA) with the infrastructure where it is integrated. | Man | Supportability | |
| SvcQC.Sup04 | Service Level Agreement (SLA) | The Service MAY include Service Level Agreement (SLA) with user communities. | Aut | Supportability | |
| SvcQC.Mon01 | Monitoring Operational Production State |The Service in an operational production state SHOULD be monitored for functional-related criteria. | Aut | Availability, Reliability | |
| SvcQC.Mon01.1 | Monitoring Service Public endpoints |The Service public endpoints MUST be monitored. | Aut | Availability, Reliability | |
| SvcQC.Mon01.2 | Monitoring Service public APIs |The Service public APIs MUST be monitored. Use functional tests. | Aut | Availability, Reliability | |
| SvcQC.Mon01.3 | Monitoring Service Web Interface |The Service Web interface MAY be monitored. Use functional tests. | Aut | Availability, Reliability | |
| SvcQC.Mon02 | Monitoring Security |The Service MUST be monitored for security-related criteria. | Aut | Availability, Reliability | |
| SvcQC.Mon02.1 | Monitoring Security Public endpoints and APIs |The Service MUST be monitored for public endpoints and APIs secured and strong ciphers for encryption. Use Security tests of criteria [SvcQC.Sec02] and [SvcQC.Sec05]. | Aut | Availability, Reliability | |
| SvcQC.Mon02.2 | Monitoring Security DAST | The Service SHOULD be monitored with DAST checks. Use Security tests of criteria [SvcQC.Sec06]. | Aut | Availability, Reliability | |
| SvcQC.Mon03 | Monitoring Infrastructure | The Service MUST be monitored for infrastructure-related criteria. | Aut | Availability, Reliability | |
| SvcQC.Mon03.1 | Monitoring IaC Unit tests | IaC (unit) tests SHOULD be reused as monitoring tests, thus avoiding duplication. | Aut | Availability, Reliability | |
| SvcQC.Met01 | Metrics | The Service SHOULD implement the collection of metrics. | Aut | Operability | |
| SvcQC.Met01.1 | Cumulative metrics | The collection of metrics SHOULD be cumulative over time and timestamped, so that the values can be queried per time interval. | Aut | Operability | |
| SvcQC.Met01.2 | Metrics Registered users | The metric Number of registered users SHOULD be collected. | Aut | Operability | |
| SvcQC.Met01.3 | Metrics Active users | The metric Number of active users over a given period of time MAY be collected. | Aut | Operability | |
| SvcQC.Met01.4 | Metrics Computing resources | The metric Amount of computing resources per user or per group MAY be collected. The metric unit depends on the type of service and infrastructure. An example is CPU x hours. | Aut | Operability | |
| SvcQC.Met01.5 | Metrics Storage resources | The metric Amount of storage resources per user or per group MAY be collected. The metric unit depends on the type of service and infrastructure. An example is GByte x hours. | Aut | Operability | |

