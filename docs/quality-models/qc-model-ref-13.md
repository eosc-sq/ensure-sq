# QM Reference 13: (paper ID = 150)

Reviewer: MD (Mario David)

CESSDA Software Maturity Levels, John Shepherdson
<https://zenodo.org/record/2614050>

Define 5 levels of maturity:

* SML1 - Initial usability; software use is not recommended.
* SML2 - Use is feasible; the software can be used by skilled personnel but
  with considerable effort, cost and risk. Assessment of effort, cost and 
  risk shall be made before use is attempted.
* SML3 - Use is possible by most users; with some effort, cost, and risk. A 
  risk assessment should be made before use.
* SML4 - Software is usable; with little effort, cost, and risk.
* SML5 - Demonstrable usability; there is clear evidence that the software
  is widely used by many users. *This is what is described in the definition*.

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Characteristics | Comment |
| :------: | :---: | :--------: | :-----------------: | :-------------: | :-----: |
| CA1   | Documentation             | | Man | Supportability | |
| CA1.1 | End-user Documentation    | ​User materials and tutorials can be used as training resources. There is detailed in-software contextual user support documentation. Documentation is consistent with current version of the software. User created documentation and comments form part of the documentation available. | Man | Supportability | |
| CA1.2 | Operational Documentation | ​Documentation is appropriate for different categories of deployment and management of the software. Deployment and configuration demonstrations, materials and tutorials can be used to teach other users. Documentation is consistent with current version of the software. User created documentation and comments form part of the documentation available. | Man | Supportability | |
| CA1.3 | Development Documentation | All stages of the software development lifecycle are fully documented, including design, testing and future improvement planning. Documentation is appropriate for different categories of users. Documentation describes the current version of the software. User created documentation and comments form part of the documentation available.| Man | Supportability | |
| CA2   | Intellectual Property | There are multiple statements embedded into the software product describing unrestricted rights and any conditions for use, including commercial and non-commercial use, and the recommended citation. The list of developers is embedded in the source code of the product, in the documentation, and in the expression of the software upon execution. The intellectual property rights statements are expressed in legal language, machine-readable code, and in concise statements in language that can be understood by laypersons, such as a pre-written, recognizable license. | Aut | Supportability | |
| C3    | Extensibility | There is evidence that the software has been extended externally by users outside of the original development group using existing documentation only. There is a clear approach for modifying and extending features across a in multiple scenarios, with specific documentation and features to allow the building of extensions which are used across a range of domains by multiple user groups. There may be a library available of user-generated content for extensions and user  generated documentation on extension is also available. | Man | Attractiveness | |
| CA4   | Modularity             | ​It is evident that all functions and data are encapsulated into objects or accessible through web service interfaces. There is consistent error handling with meaningful messages and advice, and use of generic extensions to program languages for stronger type checking and compilation-time error checking. Services are available externally and code within each module contains few independent logical paths. | Aut | Functional suitability | |
| CA5   | Packaging             | A Continuous Integration server job (or equivalent) is available to deploy the packaged/containerised software.Administrators are notified if deployment fails. Versions of deployed software can be upgraded/rolled back from a Continuous Integration server job (or equivalent). Data and/or index files can be restored from a Continuous Integration server job (or equivalent). | Aut | Installability | |
| CA6   | Portability             | The software is completely portable to the target platform. In theory at least, the software will run on the target platform provided it is packaged/containerised. | Aut | Portability | |
| CA7   | Standards Compliance | ​Compliance with open or internationally recognized standards for the software and software development process, is evident and documented, and verified through testing of all components.Ideally independent verification is documented through regular testing and certification from an independent group. | Aut | Functional suitability | |
| CA8   | Support             | The support by the organisation(s) is clearly defined with frequent and timely updates, releases, etc., responding to the needs of the user communities, as well as consolidation of changes by the community. There is a staffed telephone/email helpdesk available as well as a maintained website. Discussion groups are active and include regular input from the developer(s) and developer organisation(s). There is evidence that continuity of support is implied. Support may be free or fee-based via a support Service Level Agreement (SLA) with the developer(s) or a third party. | Man | Maintainability, Operability | |
| CA9   | Verification and Testing | Actual software application tested and validated through successful use of application output. | Aut | Functional suitability | |
| CA10  | Security             | Security was addressed in the development phases up to and including product release. | Aut | Security | |
| CA11  | Internationalisation and Localisation | Demonstrable usability: Software has been tested with multiple pseudo or genuine translations. | Man | Technical accessibility, Usability | |
| CA12  | Authentication and Authorisation | Full rights management by users, sharing/delegation of permissions/access to individual data from within the system. | Aut | Security, Technical accessibility | |
