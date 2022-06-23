# QM Reference 14: (paper ID = 151)

Reviewer: CL (Cerlane Leong)

A set of common software quality assurance baseline criteria for research projects, Pablo Orviz, et al.
<https://digital.csic.es/handle/10261/160086>

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Category | Comment |
| :------: | :---: | :--------: | :-----------------: | :------: | :-----: |
|CA1  |Open source and publicly available | Following the open-source model, the source code being produced MUST be open and publicly available to promote the adoption and augment the visibility of the software developments.| Manuel |Code Accessibility (Availability, Usability, Atrractiveness) | |
|CA2 | Version Control System |Source code MUST use a Version Control System (VCS).It is RECOMMENDED that all software components delivered by the same project agree on a common VCS. | Manual |Code Accessibility (Technical accessibility)  | |
|CA3 | Source code residency |Source code produced within the scope of a broader development project SHOULD reside in a common organization of a version control repository hosting service. | Manual |Code Accessibility (Technical accessibility and Attractiveness) | |
|L1 |Open-source license |As open-source software, source code MUST adhere to an open-source license to be freely used, modified and distributed by others. Non-licensed software is exclusive copyright by default.  | Manual | Licensing | |
|L2 |Open Source Definition |License MUST be compliant with the Open Source Definition. RECOMMENDED licenses are listed in the Open Source Initiative portal under the Popular Licenses category. |Manual |Licensing  | |
|L3 | Presence of licenses |Licenses MUST be physically present (e.g. as a LICENSE file) in the root of all the source code repositories related to the software component. |Manual |Licensing | |
|CW1 |Working state version | The main branch in the source code repository MUST maintain a working state version of the software component. Main branch SHOULD be protected to disallow force pushing, thus preventing untested and unreviewed source code from entering the production-ready version. New features SHOULD only be merged in the main branch whenever the SQA criteria is fulfilled. | Automatic/Manual | Code Workflow (Maintainability) | |
|CW2 |Change Branches |New changes in the source code MUST be placed in individual branches. It is RECOMMENDED to agree on a branch nomenclature, usually by prefixing, to differentiate change types (e.g. feature, release, fix). | Manual | Code Workflow (Maintainability) | |
|CW3 |Secondary long-term branch |The existence of a secondary long-term branch that contains the changes for the next release is RECOMMENDED. Next release changes come from the individual branches. Once ready for release, changes in the secondary long-term branch are merged into the main branch and versioned. At that point in time, main and secondary branches are aligned. This step SHOULD mark a production release.  |Manual |Code Workflow (Maintainability) | |
|CW4 | Semantic Versioning specification |Semantic Versioning specification is RECOMMENDED for tagging the production releases. |Manual  |Code Workflow (Maintainability) | |
|CS1 |Compliance with de-facto style standard |Each individual software product MUST comply with a de-facto code style standard for all the programming languages used in the codebase. Compliance with multiple standards MAY exist.  |Manual |Code Style (Maintainability) | |
|CS2 |Avoid custom code style guidelines |Custom code style guidelines MUST be avoided, only considered in the hypothetical event of programming languages without existing community style standards. Custom styles MUST be documented by defining each convention and its expected output. Custom styles SHOULD evolve over time towards a more consistent definition.  |Manual |Code Style (Maintainability) | |
|CS3 |Allow exceptions |Exceptions of individual conventions from the main definition are allowed but SHOULD be avoided. Absence of standard conventions SHOULD be justified and tracked.  |Manual |Code Style (Maintainability) | |
|CS4 |Automated code style compliance testing |Code style compliance testing MUST be automated and MUST be triggered for each candidate change in the source code. | Automatic |Code Style (Maintainability) | |
|UT1 |Minimum acceptable code coverage |Minimum acceptable code coverage threshold SHOULD be 70%. Unit testing coverage SHOULD be higher for those sections of the code identified as critical by the developers, such as units part of a security module. Unit testing coverage MAY be lower for external libraries or pieces of code not maintained within the product's code base.  | Automatic |Unit Testing | |
|UT2 |Separation of main code and units |Units SHOULD reside in the repository code base but separated from the main code. |Manual  |Unit Testing | |
|UT3 |Unit testing coverage checks |Unit testing coverage MUST be checked on change basis. |Autoamtic |Unit Testing | |
|UT4 |Unit testing coverage automation |Unit testing coverage MUST be automated. When working on automated testing, the use of testing doubles is RECOMMENDED to mimic a simplistic behaviour of objects and procedures. |Automatic |Unit Testing | |
|FT1 |Test coverage |Functional testing SHOULD tend to cover the full set of functionality that the software component claims to provide. |Manual |Functional Testing | |
|FT2 |Automated checks |Functional tests SHOULD be checked automatically with the exception of those functionality that require human interaction, such as Graphical User Interfaces (GUI). | Automatic/Manual |Functional Testing | |
|FT3 |Testing doubles |When working on automated testing, the use of testing doubles is RECOMMENDED to mimic a simplistic behaviour of objects and procedures. |Automatic |Functional Testing | |
|FT4 |Functional test code base |Functional tests SHOULD reside in the software component repository code base but separated from the main code. |Manual |Functional Testing | |
|FT5 |Regression testing |Regression testing, that checks the conformance with previous tests, is covered at this stage by executing the complete set of functional tests available. |Automatic |Functional Testing | |
|FT6 |Check testings |Functional and regression testing MUST be checked on change basis. |Manual |Functional Testing | |
|FT7 |Coverage and automation suitability |Functional and regression testing coverage MAY NOT be suitable for automated testing. |Manual |Functional Testing | |
|IT1 |Outcome and operation |Integration testing outcome MUST guarantee the overall operation of the software component whenever new functionality are involved. |Automatic/Manual |Integration Testing | |
|IT2 |Acceptance and Scalability Testing |Integration testing MAY be complemented with Acceptance and Scalability testing. |Manual |Integration Testing | |
|IT3 |Unsuitable for Automated testing |Integration testing MAY NOT be suitable for automated testing. |Manual |Integration Testing | |
|IT4 |Pilot service ifnrastructures or local testbeds |On lack of automation, pilot service infrastructures or local testbeds MAY be used. |Manual |Integration Testing | |
|IT5 |Viability of Integration Testing |Integration testing MAY NOT be viable to be checked on change basis, as it is likely to involve complex scenarios. |Manual |Integration Testing | |
|D1 |Documentation as Code |Documentation MUST be treated as code. Version controlled, it MAY reside in the same repository where the source code lies. | Manual  | Documentation| |
|D2 |Plain text using markup language |Documentation MUST use plain text format using a markup language, such as Markdown or reStructuredText. It is RECOMMENDED that all software components delivered by the same project agree on a common markup language.  |Manual |Documentation | |
|D3 |Available online |Documentation MUST be online available in a documentation repository. Documentation SHOULD be rendered automatically. |Automatic |Documentation | |
|D4 |Documentation updates with new software versions |Documentation MUST be updated on new software versions involving any substantial or minimal change in the behaviour of the application. |Automatic/Manual |Documentation | |
|D5 |Documenation updates if inaccurate/unclear |Documentation MUST be updated whenever reported as inaccurate or unclear. |Manual |Documentation | |
|D6 |Documentation production |Documentation MUST be produced according to the target audience, varying according to the software component specification. The identified types of documentation and their RECOMMENDED content are README file(one-paragraph description of the application, a "Getting Started" step-by-step description on how to get a development enviroment running, automated test execution how-to, links to external documentation below, contributing code of coduct, versioning specification, author list and contacts, license information and acknowledgements), Developer documentations (Private API documentation, structure and interfaces and build documentation), Deployment and Aministration documentations (Installation and configuration guides, service reference card, FAQs and troubleshooting) and user documentations (Public API documentation and command-line reference). |Manual |Documentation | |
|D7 |Documentation checks |Documentation MUST be checked on change basis. |Automatic/Manual | Documentation| |
|S1 |OWASP Compliance |Compliance with Open Web Application Security Project (OWASP) secure coding guidelines is RECOMMENDED, even for non-web applications. |Manual |Security | |
|S2 |Static application security testing (SAST) |Source code SHALL use automated linter tools to perform static application security testing (SAST) that flag common suspicious constructs that may cause a bug or lead to a security risk (e.g. inconsistent data structure sizes or unused resources). |Automatic |Security | |
|S3 |Dynamic application security testing (DAST) |Dynamic application security testing (DAST) SHALL be performed from the outside, to software components in an operating state, to look for security vulnerabilities (e.g. SQL injection, cross-site scripting). |Automatic |Security | |
|S4 |Manual penetration testing | Manual penetration testing MAY be part of the application security verification effort.|Manual |Security | |
|S5 |Security code reviews |Security code reviews for certain vulnerabilities SHOULD be done as part of the identification of potential security flaws in the code. Inputs SHOULD come from automated linters and manual penetration testing results. |Automatic/Manual |Security | |
|S6 |Files & Directories presence |World-writable files or directories MUST NOT be present in the product's configuration or logging locations. |Manual |Security | |
|S7 |Files & Directories creation |World-writable files SHOULD NOT be created while the service is in operation. Whenever they are required, the relevant files MUST be documented. |Manual |Security | |
|S8 |Files and passwords |World-readable files MUST NOT contain passwords. |Manual |Security | |
|S9 |Service delivery at operational level |The services delivered SHALL adhere to any extra security policies or requirements set at the operational level. |Manual |Security | |
|CR1 |Code review functionality |Code reviews MUST be done in the agreed peer review tool within the project, with the following RECOMMENDED functionality: (a) Allows general and specific comments on the line or lines that need to be reviewed. (b) Shows the results of the required change-based test executions. (c) Allows to prevent merges of the candidate change whenever not all the required tests are successful. \\Exceptions to this rule cover the third-party or upstream contributions which MAY use the existing mechanisms or tools for code review provided by the target software project. This exception MUST only be allowed whenever the external revision lifecycle does not interfere with the project deadlines. |Manual |Code Review  (Maintainability) | |
|CR2 |Open and collaborative |Code reviews MUST be open and collaborative, allowing external expert revisions. |Manual |Code Review  (Maintainability) | |
|CR3 |Lightweight and Informal |Code reviews SHOULD be lightweight and informal, meaning that some of the areas the reviewers MAY focus are: (a) Message description: commit message is clear, self-explanatory and describes precisely the objectives being addressed. (b) Goal or scope: change is needed and/or addresses/fixes the whole set of objectives. (c) Code analysis: useless statements in the code, library or modules imported but never used or code style suggestions. (d) Review of required tests: current battery of tests is sufficient for validation. (e) Review of documentation: whether the change SHOULD bring along a corresponding update in the documentation. |Manual |Code Review (Usability and Maintainability) | |
|CR4 |Code review checks |Code reviews MUST be checked on change basis. |Automatic/Manual |Code Review (Maintainability) | |
|CR5 |Security risk assessments |Code reviews SHOULD assess the inherent security risk of the changes, ensuring that the security model has not been downgraded or compromised by the changes. |Manul |Code Review (Security and Maintainability)| |
|AD1 |SCM module as code |A software configuration management (SCM) moduleis treated as code. Version controlled, it SHOULD reside in a different repository than the source code to facilitate the distribution. |Manual |Automated Deployment (Operability) | |
|AD2 |SCM tool |It is RECOMMENDED that all software components delivered by the same project agree on a common SCM tool. However, software products are not restricted to provide a unique solution for the automated deployment. |Manual |Automated Deployment (Operability) | |
|AD3 |Changes |Any change affecting the application�s deployment or operation MUST be subsequently reflected in the relevant SCM modules. |Manual |Automated Deployment (Operability) | |
|AD4 |Official repositories |Official repositories provided by the manufacturer SHOULD be used to host the SCM modules, thus augmenting the visibility and promote external collaboration. |Manual |Automated Deployment (Operability) | |


## Category

* Code Accessibility
* Licensing
* Code Workflow
* Code Style
* Unit Testing
* Functional Testing
* Integration Testing
* Documentation
* Security
* Code Review
* Automated Deployment 
