# Papers that where reviewed

## Template

Table columns of template:

* Paper_id: paper id in the list below, for example ID = 11 for the first paper.
* Name: name of criteria.
* Definition: description/summary of the criteria.
* Qualitative/quantitative: if the criteria is objective/measurable (possible to automate) or
  subjective and difficult to automate.
* Targeted to SW (see <https://github.com/eosc-sq/overleaf-ensure-sq/blob/main/landscaping.tex>):
  at the, moment one of:
  * Library
  * Framework
  * Application (such as Monte-Carlo simulation)
  * Analysis script
  * Services and platforms
* Reviewer(s): reviewer short name, for example DG for Daniel Garijo, see below.
* Comment: any other comment the reviewer sees fit to make.

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
|          |       |            |                          |                |           |         |

## Reviewers

* DG - Daniel Garijo
* ER - Elisabetta Ronchieri
* JC - Leyla Jael Castro
* LC - Laura del Cano
* MC - Miguel Colom
* MD - Mario David
* MT - Massimo Torquati
* MV - Maxime Van den Bossche
* VL - Violaine Louvet
* IC - Isabel Campos
* CL - Cerlane Leong

## 11 - Software quality through the eyes of the end-user and static analysis tools: A study on Android OSS applications

Srisopha K., Alfayez R.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-85051522416&doi=10.1145%2f3194095.3194096&partnerID=40&md5=7a9dc5d4116e134e2a85128cb3328d90>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 11       | Code complexity      |  Paper does not provide a definition, but the less complex the code is, the better          |  Quantitative  | all types | DG        | See below    |
| 11       | Number of code smells      |  certain structures in the code which indicate a violation of fundamental design principles. The lower code smells, the better. Ref: Martin Fowler and Kent Beck. 1999. Refactoring: improving the design of existing code. Addison-Wesley Professional.  | Quanticative | all types | DG        | See below    |
| 11       | Comment density      | The idea here is that better commented code is easier to understand | Quantitative  | all types | DG        | See below    |
| 11       | User reviews      | The paper attempts to find correlation between user reviews and code quality. However, "to some extent, having high or low code quality does not necessary ensure user satisfaction" | Quantitative | apps with a store | DG        | See below    |
| 11       | PMD quality metrics     | Empty code, Naming, Braces, Import statements, Coupling, Unused Code, Unnecessary, Design, Optimization, String and StringBuffer | Quantitative | apps with a store | DG        | See below    |
| 11       | Findbugs quality metrics      | Dodgy code, Bad practice, Malicious code, Performance, Correctness, Security, Multithreaded correctness, Internalization | Quantitative | apps with a store | DG        | See below    |

**Quality Model** ("is based on", "mentions"): ISO/IEC 25010

This paper proposes a quality analysis from an empirical point of view. It uses three tools for
quantitative analysis: SonarQube, PMD and FindBugs. The quality metrics are not proposed per se in
the paper, but are useful candidates.

The paper mentions ISO/IEC 25010 software product quality characteristics. These are:

* functional suitability
* performance efficiency
* usability
* portability
* compatibility
* reliability
* maintainability
* security

The following table shows how each tool tackles different metrics. However, some are not defined:

|Abbr.| Tool      | Metric|
|:---:|:---------:|:-----:|
| CS  | SonarQube | Number of code smells|
| PD  | PMD       | Empty code, Naming, Braces, Import statements, Coupling, Unused Code, Unnecessary, Design, Optimization, String and StringBuffer|
| FB  | FindBugs  | Dodgy code, Bad practice, Malicious code, Performance, Correctness, Security, Multithreaded correctness, Internalization|

## 41 - Fostering software quality assessment

Brandtner M.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-84886382849&doi=10.1109%2fICSE.2013.6606725&partnerID=40&md5=9e042076903be6351b3b97be6a877cb3>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 41       | Individual Information | Stakeholder's information influenced by the role involved and the type of software. |  Qualitative  |  All  | ER | Type of software can be rich client, web application and so on. |
| 41       | Stakeholder context | Detail e.g. stakeholder role and tool-usage data by each stakeholder |  Qualitative |  All | ER        |  Software architects, developers and testers are the considered essential role in the development process. |
| 41       | Technical context | Information about the source code by using e.g. software metrics |  Quantitative |  All | ER        |  Type of software can be rich client, web application and son. |
| 41       | Context-sensitive | The relation between the data, the world the data refers to, and the observer's expectations, intentions and interests |  Qualitative |  All | ER        |  The paper provides an illustrative example to support different stakeholders in the quality assessment of a software system. |

**Quality Model** ("is based on", "mentions"): Own metrics

**NOTE: This article is mainly on software quality assessment than software quality definition.**
However it contains an interesting approach based on stakeholder's information needs and the
tailoring of information for software quality assessment. This paper also provides some guidelines
to support the activities carried out by each type of stakeholders.

## 45 - A systematic review of quality attributes and measures for software product lines

Montagud S., Abrahão S., Insfran E.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-84865626740&doi=10.1007%2fs11219-011-9146-7&partnerID=40&md5=33b25cd0a25fc09685e06cbc9c988f14>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
 | 45 | Binary size | Binary size | Quantitative |  | JC | Exclude, not sure how good this criterion is |
 | 45 | Complexity of the source code | Cyclomatic complexity | Quantitative |  | JC |  |
 | 45 | Performance |  | Quantitative |  | JC |  |
 | 45 | Complexity of the source code (for classes and components) |  | Quantitative |  | JC | Requires well established software engineering practices.  Alternative: Yes/No and how (e.g., code review) |
 | 45 | Complexity of diagrams (for classes and components) |  | Quantitative |  | JC | Requires well established software engineering practices. Alternative: Yes/No and how (e.g., some sort of peer-review) |
 | 45  | Complexity of an architecture |  | Quantitative |  | JC | Requires well established software engineering practices. Alternative: Yes/No and how (e.g., some sort of peer-review) |
 | 45 | Complexity of a use case |  | Quantitative |  | JC | Requires well established software engineering practices. Alternative: Yes/No and how (e.g., some sort of peer-review) |
 | 45 | Complexity of a use case diagram |  | Quantitative |  | JC | Optional, not sure use case diagrams are always needed. Exclude |
 | 45 | Maintainability Index (MI) (for the whole, for a component, for the architecture |  | Quantitative |  | JC |  |
 | 45 | Reusability (of the whole and the components) |  | Quantitative |  | JC |  |
 | 45 | Reusability of the architecture |  | Quantitative |  | JC |  |
 | 45 | Applicability |  | Quantitative |  | JC | Validation against use cases or requirements (?) |
 | 45 | Understandability |  | Quantitative |  | JC |  |
 | 45 | Efficiency |  | Quantitative |  | JC | Exclude (difficult to measure) |
 | 45 | Effort required for changes |  | Quantitative |  | JC | Exclude (difficult to measure) |
 | 45 | Size (of modules, lines, components) |  | Quantitative |  | JC | Exclude, not sure how good this criterion is |
 | 45 | Maturity | Time for the code to fail, number of resolved bugs, number of open bugs | Quantitative |  | JC |  |
 | 45 | Configuration Complexity |  | Quantitative |  | JC | Configuration to run the code (?) |
 | 45 | Modularity of the architecture |  | Quantitative |  | JC |  |
 | 45 | Customizability |  | Quantitative |  | JC | Exclude, looks like related to customization by final user |
 | 45 | Internal cohesion |  | Quantitative |  | JC | Exclude (difficult to measure). Requires well established software engineering practices |
 | 45 | Coherence |  | Quantitative |  | JC | Exclude (difficult to measure). Requires well established software engineering practices |

**Quality Model** ("is based on", "mentions"): Own metrics. (**mdavid**) TO BE Discussed if what
metrics can be taken from this paper.

## 46 - Standardized code quality benchmarking for improving software maintainability

Baggen R., Correia J.P., Schill K., Visser J.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-84860465895&doi=10.1007%2fs11219-011-9144-9&partnerID=40&md5=042a7624f2cb95e1a97643ef8e0f9071>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 46       | Volume | Size of the software application | Quantitative | All Types | LC        | Estimated rebuild value |
| 46       | Redundancy | Level of redundancy in code | Quantitative | All Types | LC        | Percentage of redundant code |
| 46       | Unit size | Lowel-level piece of functionality that should be maintained | Quantitative | All Types | LC        | Lines of code per unit (Unit=smallest piece of invokable code) code |
| 46       | Unit complexity | Of the software application | Quantitative | All Types | LC        | Cyclomatic complexity per unit |
| 46       | Unit interface size | Number of parameters in interface | Quantitative | All Types | LC        | Number of parameters per unit |
| 46       | Module coupling |  | Quantitative | All Types | LC        | Number of parameters per unit | Number of incoming calls per module |
| 46       | Analysability | measured with Volume, Redundancy and Unit size | Quantitative | All Types | LC        | ISO/IEC 9126 |
| 46       | Changeability | measure with Redundancy, Unit complexity and Module coupling | Quantitative | All Types | LC        | ISO/IEC 9126 |
| 46       | Stability | measured with Unit inteface size and Module coupling | Quantitative | All Types | LC        | ISO/IEC 9126 |
| 46       | Testability | measured with Unit complexity and Unit size | Quantitative | All Types | LC        | ISO/IEC 9126 |
| 46       | Maintainability |  | Quantitative | All Types | LC        | ISO/IEC 9126 |

**Quality Model** ("is based on", "mentions"): ISO/IEC 9126

The paper presents a standardized measurement model based on the ISO/IEC 9126 definition of
maintainability and source code metrics. In this ISO standard they propose a hierarchical quality
model made of quality characteristics decomposed in sub-characteristics. They choose 6 code
properties as key metrics for the quality assessment of the sub-characteristics.
Then they keep a benchmark database to perform comparison and evaluate new measurements. In this
database they use metadata attributes to tag each measurement and help with comparing.

The quality characteristics from ISO/IEC 9126 they mention are:

* Analysability: measured with Volume, Redundancy and Unit size.
* Changeability: measure with Redundancy, Unit complexity and Module coupling.
* Stability: measured with Unit interface size and Module coupling.
* Testability: measured with Unit complexity and Unit size.

## 58 - Quality specification and metrication, results from a case-study in a mission-critical software domain

Trienekens J.J.M., Kusters R.J., Brussel D.C.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-77956057048&doi=10.1007%2fs11219-010-9101-z&partnerID=40&md5=8676a4867b80d63fce5b0d10d732fb63>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 58 | real-time performance |  | Quantitative | critical systems (non exclusive) | MC |  |
| 58 | reliability | mission specific | Quantitative | critical systems (non exclusive) | MC |  |
| 58 | consistency | same rules along SW development process | Quantitative | | MC |  |
| 58 | transparency | | Quantitative | | MC |  |
| 58 | usability | feedback from final users | Qualitative | | MC |  |
| 58 | effectiveness | useful for final users | Quantitative | | MC |  |
| 58 | productivity | fast results from final users | Quantitative | | MC |  |
| 58 | usability | easy to use by final users | Quantitative | | MC |  |
| 58 | safety |  not prone to error by final users | Quantitative | | MC |  |
| 58 | satisfaction |  feedback from final users | Qualitative | | MC |  |
| 58 | maintainability |  Easy to modify according to changing needs | Quantitative | | MC |  |
| 58 | portability | Easy to implement in different scenarios | Quantitative | | MC |  |

**Quality Model** ("is based on", "mentions"): ISO/IEC 9126

## 85 - Achieving quality in open-source software

Aberdour M.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-33846917203&doi=10.1109%2fMS.2007.2&partnerID=40&md5=08d47741430e05c8a0ceb015a1f43a04>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 85       | Code documentation | The code is documented      | Qualitative and quantitative | all types | DG        | See below |
| 85       | Sustainable community | Is there an active community behind the software product? (i.e., for maintenance/bug fixing) | both |  all types              | DG        | See below |
| 85       | Code modularity   | The code of the project is not a whole entity, but is fragmented in smaller modulues that make it easier to contribute to | Quantitative | all types | DG        | See below |
| 85       | Code goes through code reviews/peer review | Each contribution is assessed by a contributor different from the author |  Qualitative                        | All types  | DG        | See below |
| 85       | Tests | Each method/function has a test to support it | Quantitative | all types | DG        | See below |
| 85       | Tutorials | Availability of material explaining how to use the target software through examples | Qualitative/Quantitative | All types  | DG        | See below |

**Quality Model** ("is based on", "mentions"): Own metrics. (OpenSource SW)

The paper focuses on project management for quality, comparing open source software projects with
non open initiatives.

* Quality areas: quality assurance (focuses on process and procedure, learning from mistakes, and
  ensuring good management practice) and quality control (process of verification and validation)

## 88 - Driving software quality: How test-driven development impacts software quality

Crispin L.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-33846907119&doi=10.1109%2fMS.2006.157&partnerID=40&md5=1c6ac14fdd83073f861f9ec5b1e95701>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 88       | Test driven development | Definition and development of unit tests for each functionality | Quantitative | All | ER |  |
| 88       | Project creole      | A shared language (between manager and developers)           | Qualitative: managers can improve the way they define features, developers can easily produce well-tailored program  | All | ER | It considers important the development of a shared language or project creole between business people and developers to find some common ground and work together in order to improve software development.  |

**Quality Model** ("is based on", "mentions"): Test Driven Development (TDD).

**NOTE: this is a paper of 2 pages**. For my point of view it can be left out for quality definition.

## 92 - Software quality development and assurance in RUP, MSF and XP -A comparative study

Zuser W., Heil S., Grechenig T.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-84885903144&doi=10.1145%2f1083292.1083300&partnerID=40&md5=c47fec6c93dd2cc890ba61b5ce2ab7c1>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 92 | Customer satisfaction |  | Quantitative (e.g., surveys) |  | JC | Not sure applicable for research sw |
| 92 | Functional requirements | Yes or not release adheres to functional requirements | Quantitative |  | JC | Useful but not sure how it would work for research sw |
| 92 | Usability | Easy of usage by end users | Quantitative (e.g., surveys) |  | JC | Not easy for research sw |
| 92 | Architecture design | Arhitecture showing modules and interactions | Qualitative |  | JC | Not easy for research sw  |
| 92 | Team work  | Pair programming, code review | ??? |  | JC  | Should be split into more granular criteria |

**Quality Model** ("is based on", "mentions"): Own metrics.

## 93 - Early estimation of software quality using in-process testing metrics: A controlled case study

Nagappan N., Williams L., Vouk M., Osborne J.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-77955433687&doi=10.1145%2f1083292.1083304&partnerID=40&md5=c3b21a87b407b65539153ab3017b0eda>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 93       | Test quantification SM1 | Number of Assertions SLOC* | Quantitative | Java code | LC        | Accounts for coding/testng style |
| 93       | Test quantification SM2 | Number of Test Cases SLOC* | Quantitative | Java code | LC        | Accounts for coding/testng style |
| 93       | Test quantification SM3 | Number of Assertions divided by Number of Test Cases | Quantitative | Java code | LC        | Accounts for coding/testng style |
| 93       | Test quantification SM4 | (TLOC/SLOC*)  divided by (Number of Classes Test Number of ClassesSource) | Quantitative | Java code | LC        | Serves as a control measure to counter the confounding effect of class size |
| 93       | Cyclomatic complexity | Relative ratio of test to source code in Cyclomatic Complexity | Quantitative | Java code | LC        | Complexity and O-O metrics |
| 93       | CBO  | Relative ratio of test to source code in Coupling between objects | Quantitative | Java code | LC        | Complexity and O-O metrics |
| 93       | DIT  | Relative ratio of test to source code in Depth of Inheritance | Quantitative | Java code | LC        | Complexity and O-O metrics |
| 93       | WMC  | Relative ratio of test to source code in  weighted methods per class | Quantitative | Java code | LC        | Complexity and O-O metrics |
| 93       | Relative size adjustment  | SLOC* divided by Minimum SLOC* | Quantitative | Java code | LC        | Complexity and O-O metrics |

**Quality Model** ("is based on", "mentions"): Own metrics. Object Oriented - JAVA.

\* Source Lines of Code (SLOC) is computed as non-blank, non-comment source lines of code

\+ Test Lines of Code (TLOC) is computed as non-blank, non-comment test lines of code

They present a metric suite called the Software Testing and Reliability Early Warning metric suite
for Java (STREW-J) that can be used as an early indication of an external measure of software
application quality. They put a greater emphasis on internal software metrics, particularly those
involving the testing effort. It requires the existence of an extensive suite of automated unit test
cases being created as development proceeds.

## 99 - The evolution path for industrial software quality evaluation methods applying ISO/IEC 9126:2001 quality model: Example of MITRE's SQAE method

Côté M.-A., Suryn W., Laporte C.Y., Martin R.A.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-17444388547&doi=10.1007%2fs11219-004-5259-6&partnerID=40&md5=09ec05c221610b4c799ab6111def6568>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: | 
| 99 | consistency | in many aspects of ISO/EIC 9126 | Quantitative | | MC |  |
| 99 | independence | interoperativity, changeability, adaptability | Quantitative | | MC |  |
| 99 | modularity | changeability, testability | Quantitative | | MC |  |
| 99 | documentation | learnability, analysability | Quantitative | | MC |  |
| 99 | self-descriptiveness | understandability, operability, analysability | Quantitative | | MC |  |
| 99 | anomaly-control | maturity, fault tolerance, recoverability, reliability compliance | Quantitative | | MC |  |
| 99 | design simplicity | security, analysability, changeability, stability, testability | Quantitative | | MC |  |

**Quality Model** ("is based on", "mentions"): ISO/IEC 9126

Mainly a correlation between their proposed quality factors and the sub-characteristics in
ISO/EIC 9126.

## 108 - Construction of a systemic quality model for evaluating a software product

Ortega M., Pérez M., Rojas T.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-3543054780&doi=10.1023%2fA%3a1025166710988&partnerID=40&md5=f6915840807fb5204c5c331644d47524>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 108      | Systemic model | Extends ISO9126, Dromey and McCall models  |  Mainly qualitative: set of measures and practices   |   all   | MT   | See below     |

**Quality Model** ("is based on", "mentions"): Extends ISO9126, Dromey and McCall models.

Comment

The study proposes a systemic quality model. Authors developed a process framework with which to
evaluate product quality considering the processes that contribute to product quality. They
basically extend ISO 9126 product quality model considering the roles of stakeholders (project
managers, developers, and users) trying to evaluate the internal quality, which includes
functionality, reliability, usability, efficiency, maintainability, and portability characteristics.
Authors claimed that those quantities relate to each other and must be integrated for a systemic
global quality design. The work does not analyze the effect of the method applied on different
stakeholders.

## 124 - Software quality: the elusive target

Kitchenham Barbara, Pfleeger Shari Lawrence

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-0029779819&doi=10.1109%2f52.476281&partnerID=40&md5=0c903484c06cd79cb57e3161badfff3d>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 124      | quality      | For the transcendetal view, quality is something that can be recognized but not defined.  | Qualitative | Alwasys true  | ER | This view is similar to Plato's description of the ideal or Aristotele's concept of form: software quality is something we strive as an ideal. |
| 124      | quality      | For the user view, quality fits for purpose.  | Quantitative | Alwasys true  | ER | This view is quite concrete, grounded in product characteristics that meet's the user needs. |
| 124      | quality      | For the manufacturing view, quality is something that is conformant to specification.  | Quantitative | Alwasys true  | ER | This view focuses on product quality during production and after delivery. This definition is also adpted by `ISO 9001` and the `Capability Maturity Model`.|
| 124      | quality      | For the product view, quality is tied to inherent characteristics of the product.  | Quantitative | Alwasys true  | ER | This view looks inside the code, by considering the product's inehrent characteristics and measuring internal properties through software metrics.|
| 124      | quality      | For the value-based view, quality is dependent on the amount a customer is willing to pay for it.  | Quantitative | Alwasys true  | ER | This view considers the various groups views in software development and aims at avoiding misunderstanding.|
| 124      | reliability      | How long the product functions properly between failures. | Quantitative | Alwasys true  | ER | Reliability models plot the number of failures over time. This characteristic is of users'interest.|
| 124      | usability      | How the product easily supports installation, learning and use according to Tom Gilb. | Quantitative | Alwasys true  | ER | Gilb's technique can be generalized to any quality feature. This characteristic is of users'interest.|
| 124      | defect counts      | They are the number of known defects recorded against a product during development and use. | Quantitative | Alwasys true  | ER | Defects can be categorized according to the phase or activity where the defect was introduced. This characteristic is of manufacturing'interest.|
| 124      | rework costs      | It represents the staff effort spent correcting defects before and after release. | Quantitative | Alwasys true  | ER | This characteristic is of manufacturing'interest.|

**Quality Model** ("is based on", "mentions"): Extends ISO9126, Dromey and McCall models.

This paper talks about modeling quality:

* McCall's quality model (11 quality factors) J.A. McCall, P.K. Richard, G. F. Walters, "Factors in
  Software Quality", vol 1., 2. and 3, AD/A-049-014/015/055, Nat'l Tech. Information Service,
  Springfield, Va., 1977
* ISO 9126 V. Basili and D. Rombach, "The TAME Project: Towards Improvement-Oriented Software
  Environments", IEEE Trans. Software Eng. , June 1989, pp 758-773
* Dromey's model G. Dromey, "A model for software-product quality", IEEE Trans. Software Eng., Feb.
  1995.

There are several differences between ISO 9126 and McCall's model. The main problem is the
terminology used and the lack of rationale for determining which factors/characteristics should be
included in the quality definition. Dromey's model allows to determine if a model is incomplete.

## 128 - Experiences of software quality management using metrics through the life-cycle

Ogasawara Hideto, Yamada Atsushi, Kojo Michiko

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-0029516009&partnerID=40&md5=68106def0b53f2f1a609753364cb4705>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 128 | Code complexity | How convoluted or not is a code | Quantitative (e.g., Mc Cabe and Halstead metrics) |  | JC | Not easy to understand by developers (comment from paper) |
| 128 | At file level - number of modules |  | Quantitative |  | JC | For all of these criteria, what would be the acceptable metric/level? |
| 128 | At file level - number of total steps |  | Quantitative |  | JC |  |
| 128 | At file level - number of imports/dependencies |  | Quantitative |  | JC |  |
| 128 | At module level - number of steps |  | Quantitative |  | JC |  |
| 128 | At module level - number of conditions |  | Quantitative |  | JC |  |
| 128 | At module level -  number of loops |  | Quantitative |  | JC |  |
| 128 | At module level - number of arguments |  | Quantitative |  | JC |  |
| 128 | At module level - number of comments |  | Quantitative |  | JC |  |
| 128 | At module level - number of procedures |  | Quantitative |  | JC |  |
| 128 | At system level - number of modules |  | Quantitative |  | JC |  |
| 128 | At system level - number of procedures |  | Quantitative |  | JC |  |

**Quality Model** ("is based on", "mentions"): Own metrics.

## 129 - Controlling and predicting the quality of space shuttle software using metrics

Schneidewind N.F.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-0343935307&doi=10.1007%2fBF00404649&partnerID=40&md5=b99281a03e36e4acaf4ca5067792314f>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 129      | eta1 | Unique operator count | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | eta2 | Unique operand count | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | n1 | Total operator count | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | n2 | Total operand count | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | stms | Total statement count (executable code; no comments) | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | loc | Total non-commented lines of code | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | comments | Total comment count | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | nodes | Total node count (in control graph) | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | edges | Total edge count (in control graph) | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | paths | Total path count (in control graph) | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | cycles | Total cycle count (in control path) | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | maxpath | Maximum path length (edges in control path) | Quantitative           | Space SW written in HAL/S | LC        |         |
| 129      | avepath | Average path length (edges in control graph) | Quantitative           | Space SW written in HAL/S | LC        |         |

**Quality Model** ("is based on", "mentions"): Own metrics. Space SW written in HAL/S

This is a very old paper that tries to relate quality measurements at development time with quality
predictions for production. It is only valid for a specific software used in the space shuttle.

## 140 - Modelling software quality in the commercial environment

Gillies A.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-0001332319&doi=10.1007%2fBF01720924&partnerID=40&md5=a0b468b060b629ea3ced5fefac2c2848>

| Paper_id | Name       | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :--------: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 140 | Reliability     | How often does it go wrong? How long is it unavailable? Is any information lost at recovery?                           | Quantitative | | MD | SW in operation |
| 140 | Efficiency      | The critical resources needed by the operator to carry out the critical tasks can be monitored                         | Quantitative | | MD | SW in operation |
| 140 | Security        | Measured as the resource cost expended to solve problems caused by unauthorized activity                               | Quantitative | | MD | SW in operation |
| 140 | Integrity       | Measured as the resource cost expended to solve problems caused by inconsistencies within the system                   | Quantitative | | MD | SW in operation |
| 140 | Usability       | Measured using user surveys. may also be assessed in terms o f calls upon support staff                                | Quantitative | | MD | SW in operation |
| 140 | Maintainability | Measured by the resources expended in terms o f time and cost in keeping a system up and running over a period of time | Quantitative | | MD | SW in operation |
| 140 | Adaptability    | Measured in the same way as maintainability, i.e. by the resources expended in adapting the system to meet new requirements over a period of time | Quantitative | | MD |  |
| 140 | Portability     | Measured according to Gilb's measure | Quantitative | | MD | see below |
| 140 | Timeliness      | Assessed in terms of the costs of non-delivery | Quantitative | | MD |  |
| 140 | Cost~Benefit efficiency | measured in simple financial terms. The costs of installing and maintaining the system are weighed against the assessment of business benefits | Quantitative | | MD |  |
| 140 | Ease of transition | Assessed in terms o f staff time expended. The effectiveness of transition may be assessed in terms of the quality of the resulting system particularly the area of integrity. | Quantitative  | | MD | SW in operation |
| 140 | Userfriendliness   | Measured in terms of the effect upon the effectiveness of the user. The measure of user friendliness in business terms is the productivity of the user. | Quantitative | | MD | SW in operation |

**Quality Model** ("is based on", "mentions"):

* Watts, R. (1987) Measuring Software Quality, NCC Publications Manchester.
* Gilb, T. (1988) Principles of Software Engineering Management, Addison-Wesley.

* *MD* - How different parties/stakeholders perceived a given Quality Model:
  * Analysis of Structured interviews to people from 6 different market sectors, and see how they
    interpret a set of quality attributes.
  * Attributes suggested by the author and based mainly on:
    * Watts, R. (1987) Measuring Software Quality, NCC Publications Manchester.
    * Gilb, T. (1988) Principles of Software Engineering Management, Addison-Wesley.
    * Measured in general in terms of costs of Resources (Human and Infrastructure).
  * Portability according to Gilb: P = 1 - (ET/ER)
    * P represents portability
    * ET effort required to transfer the system to a new environment
    * ER represents the effort required to establish the system in its existing environment.

## 144 - Practice of quality modeling and measurement on software life-cycle

Hirayama Masayuki, Sato Hiroyuki, Yamada Atushi, Tsuda Junichiro

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-0025022794&partnerID=40&md5=155e3e9926c8e675616e8d839798a6e1>

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 144      | ESQUT | It is a source code quality index  |  Quantitative            |  (old) C code  | MT        | See below  |

**Quality Model** ("is based on", "mentions"): Own metrics. For old C code.

The paper's main motivation is that Halstead's and McCabe's metrics are not practical and have some
limitations (in the case of programs with GOTO statements and deep nesting). The authors propose a
new quantitative metric called ESQUT-C (for C programs) considering:

* n. of GOTO statements
* n. of module exits
* n. of conditional statements
* n. of procedure blocks
* nesting level of procedure blocks
* number of executions
* number of lines (LOC)
* number of real digits

They also showed how those metrics correlate with McCabe's and Halstead's metrics.
The paper has been published in 1990.

## 146 - Quantitative evaluation of software quality

Boehm B.W., Brown J.R., Lipow M.

<https://www.scopus.com/inward/record.uri?eid=2-s2.0-85042377749&partnerID=40&md5=86df793c94725cf352a0b8b3d8227c3c>

| Paper_id |           Name            |                          Definition                          | Qualitative/Quantitative | Targeted to SW | Reviewer |                           Comment                            |
| :------: | :-----------------------: | :----------------------------------------------------------: | :----------------------: | :------------: | :------: | :----------------------------------------------------------: |
|   146    |       ACCESSIBILITY       |           facilitates selective use of its parts.            |                          |      All       |    VL    | Necessary for efficiency, testability and human engineering  |
|   146    |      ACCOUNTABILITY       | its usage can be measured; critical segments of code can be instrumented with probes to measure timing, whether specified branches are exercised, etc. |       Quantitative       |      All       |    VL    |                                                              |
|   146    |         ACCURACY          | its outputs are sufficiently precise to satisfy their intended us |       Quantitative       |      All       |    VL    |                  Necessary for reliability                   |
|   146    |      AUGMENTABILITY       | it can easily accommodate expansion in component computational functions or data storage requirements |                          |      All       |    VL    |                 Necessary for modifiability                  |
|   146    |     COMMUNICATIVENESS     | it  facilitates the specification of inputs and provides outputs whose form and content are easy to assimilate and useful. |                          |      All       |    VL    |       Necessary for testability and human engineering        |
|   146    |       COMPLETENESS        | all its parts are present and each part is fully developed.  |       Quantitative       |      All       |    VL    | External references are available and required functions are coded and present as designe |
|   146    |        CONCISENESS        |            excessive information is not present.             |       Quantitative       |      All       |    VL    | Programs are not excessively fragmented nor the same sequence of code is repeated in numerous place ... |
|   146    |        CONSISTENCY        | it contains uniform notation, terminology and symbology within itself |       Quantitative       |      All       |    VL    |        Coding standards are homogeneously adhered to         |
|   146    |    DEVICE-INDEPENDENCE    | it can be executed on computer hardware configurations other than its current on |       Quantitative       |      All       |    VL    |                  Necessary for portability                   |
|   146    |        EFFICIENCY         |     it fulfills its purpose without waste of resources.      |       Quantitative       |      All       |    VL    |              Choice of efficient algorithm ...               |
|   146    |     HUMAN ENGINEERING     | it fulfills its purpose without wasting the users' time and energy, or degrading their morale |       Qualitative        |      All       |    VL    |   Implies accessibility, robustness and communicativeness    |
|   146    |        LEGIBILITY         |     its function is easily discerned by reading the code     |       Qualitative        |      All       |    VL    |               Necessary for understandability                |
|   146    |      MAINTAINABILITY      | it facilitates updating to satisfy new requirements or to correct deficiencies. |                          |      All       |    VL    |         Code understandable, testable and modifiable         |
|   146    |       MODIFIABILITY       | it facilitates the incorporation of changes, once the nature of the desired change has been determined |                          |      All       |    VL    |                                                              |
|   146    |        PORTABILITY        | it can be operated easily and well on computer configurations other than its current one. |       Quantitative       |      All       |    VL    |             Use of standard library function ...             |
|   146    |        RELIABILITY        | it can be expected to perform it s intended functions satisfactorily |                          |      All       |    VL    | The program will compile, load and execute, producing answers of the requisite accuracy |
|   146    |        ROBUSTNESS         | it can continue to perform despite some violation of the assumptions in its specification |       Quantitative       |      All       |    VL    | The program will properly handle inputs out of range or in different format ... |
|   146    |    SELF-CONTAINEDNESS     | it performs all its explicit and implicit functions within itself . |                          |      All       |    VL    | Example of implicit functions : initialization, input checking ... |
|   146    |   SELF-DESCRIPTIVENESS    | it contains enough information for a reader to determine or verify its objectives, assumptions, constraints, inputs, outputs, components, and revision status. |       Qualitative        |      All       |    VL    |       Necessary for testability and understandability        |
|   146    |      STRUCTUREDNESS       | it possesses a definite pattern of organization of its interdependent parts. |       Qualitative        |      All       |    VL    |   Standard control structure have been followed in coding    |
|   146    |        TESTABILITY        | it facilitates the establishment of verification criteria and supports evaluation of its performance. |       Quantitative       |      All       |    VL    | requirements are match to specific modules or diagnostics capabilities are provided |
|   146    |     UNDERSTANDABILITY     |            its purpose is clear to the inspector.            |       Qualitative        |      All       |    VL    | Names are used consistently, modules are self-descriptive, ... |
|   146    | USABILITY (AS-lS UTILITY) |       it is reliable, efficient and human-engineered.        |                          |      All       |    VL    | The function performed by the program is useful elsewhere, is robust against human errors or does not require excessive core memory... |

**Quality Model** ("is based on", "mentions", "defines"): define Boehm software quality model

The article describe the Boehm software quality model. It identifies characteristics of quality
structured in a tree (see above for this characteristics). It also gives a few example of quality
metrics (Boehms wrote a book on the subject). It also explains the link between the identification
of types of error and when they appear during the software life-cycle and at which phase of the
cycle they are corrected. It shows that early application of automated and semiautomated
consistency, robustnes and self containedness checkers leads to significant improvements in software
error detection. It gives some input on quality-enhancing tools and techniques. Life cycle
activities with significant effects on software quality:

* setting software quality objectives and priorities
* performing software quality benchmarking
* using software quakity checklists
* establishing an explicit quality assurance activity
* using machine-analyzable software specifications
* ensuring testable software requirements
* using a requirements-properties matrix
* establishing standards
* using an automated code auditor for standards compliance
* performing design and code inspections

## 150 - CESSDA Software Maturity Levels

John Shepherdson

<https://zenodo.org/record/2614050>

| Paper_id | Name | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer | Comment |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   150    |  Software Maturity Levels (SMMs) (with many sub-criterion)    |       The software maturity levels provide guidance on what minimum, expectedand excellent standards look like, and will be used to evaluate the productsproduced by SPs.     |  Quantitative              |       Yes         | CL       |  For all Qualitative/Quantitative questions, I answer them as Quantiative simply because there is a level, i.e. number, one can answered when talking about the maturity levels. However the actual measurements or management can be a mix.       |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   150    |  Reuse Readiness Levels (RRLs) - used by SMMs |   Reuse Readiness Levels (RRLs), as developed by NASA Earth Science DataSystems, form the basis upon which the software maturity assessments are made. Usability is not only a political imperative of research infrastructures as they need to demonstrate a return on investment, but is also essential for growthwith limited funds and ongoing interoperability.   |  Quantitative  |  Yes   | CL       |         |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   150    |  Capability Maturity Levels (CMMs) - used in combination with RRLs for service providers   |    A framework for organising continuouts process improvement steps into five maturity levels that lay successive foundations for continuous process improvement.         |                          |   No, services (service management) | CL       |         |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   150    | Technology Readiness Levels (TRLs) - used for development of technical research Infrastructure    |  A method for estimating the maturity of technologies during the acquisition phase of a program, developed at NASA during the 1970s. The use of TRLs enables consistent, uniform discussions of technical maturity across different types of technology.     |    Quanitative    |     No, Technology   | CL       |         |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   150    |   Documentation Standard (a part of RRLs and SMMs)   |   Overall document suites: en-user, operational and development documentations.         |      Quantiative    |   Yes, documentations for software             | CL       |         |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   150    |      |            |                          |                | CL       |         |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   150    |      |            |                          |                | CL       |         |

**Quality Model** ("is based on", "mentions", "defines"): Own metrics. Based on maturity of
technologies at NASA during the 1970s

(Yes) This paper doesn't directly provides quality measurements but instead it is attempting to
define software maturity levels, sustainability/reusability. However, the maturity levels are
further broken down into sub-criteria. Two NASA defined readiness levels were mentioned or based on
to help define these sub-criteria. These readiness levels can extend to services and technologies
(Research Infrastructure). Many of these sub-criteria however, are relevant to common/known quality
software criterion. In fact, usuability and sustability are two features of quality software. As
such, this paper is of interest to software quality measurements.

## 151 - A set of common software quality assurance baseline criteria for research projects

Pablo Orviz, et al.

<https://digital.csic.es/handle/10261/160086>

| Paper_id | Name | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer | Comment |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   151    |      |            |                          |                | CL       |         |

**Quality Model** ("is based on", "mentions", "defines"): Own metrics. Based on DevOps best practices.

Yes, this paper is a consolidation of Software Quality Assurace baseline criteria from ESOC. It also
contains an applied use case (code workflow with DevOps) of the criteria.

* Code Accessibility
* Licensing
* Code Style
* Code metadata
* Unit Testing
* Test Harness
* Test-Driven Development
* Documentation
* Security
* Code Workflow
* Semantic Versioning
* Code Management
* Code Review
* Automated Delivery
* Automated Deployment

## 153 - Software Quality Models in Practice

Stefan Wagner, Klaus Lochmann, Sebastian Winter, Andreas Goeb, Michael Kläs, Sabine Nunnenmacher

<https://mediatum.ub.tum.de/doc/1110601/1110601.pdf>

The following qualities are sorted in order of importance, according to the paper.
No definitions of the quality dimensions are provided, so I don't add them to the table

| Paper_id | Name | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer | Comment |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   153    |  Functional suitability    |            |                          |                | DG       |         |
|   153    |  Availability    |            |                          |                | DG       |         |
|   153    |  Reliability    |            |                          |                | DG       |         |
|   153    |  Time behavior    |            |                          |                | DG       |         |
|   153    |  Performance    |            |                          |                | DG       |         |
|   153    |  Ease of use    |            |                          |                | DG       |         |
|   153    |  Fault tolerance    |            |                          |                | DG       |         |
|   153    |  Security    |            |                          |                | DG       |         |
|   153    |  Maintainabilityu    |            |                          |                | DG       |         |
|   153    |  Recoverability    |            |                          |                | DG       |         |
|   153    |  Operability    |            |                          |                | DG       |         |
|   153    |  Resource utilization    |            |                          |                | DG       |         |
|   153    |  Safety    |            |                          |                | DG       |         |
|   153    |  Interoperability    |            |                          |                | DG       |         |
|   153    |  Attractiveness    |            |                          |                | DG       |         |
|   153    |  Compatibility    |            |                          |                | DG       |         |
|   153    |  Installability    |            |                          |                | DG       |         |
|   153    |  Technical accessibility   |            |                          |                | DG       |         |
|   153    |  Portability  |            |                          |                | DG       |         |

**Quality Model** ("is based on", "mentions", "defines"): From most used to less used:

* company-specific
* quality gates
* defect classification
* ISO 9126
* Laws
* CMMI
* ISO 9001
* ISO 250000
* Rel. Groth.

**Summary**: The paper/thesis focuses on practitioners to examine software quality models in
practice. Three main aspects of quality are dealt with: usage of QMs, importance of quality
attributes and the potential improvements to QMs.

* Focused in industry. Results reported through a survey.
* Quality models are usually adapted to respondent needs.
* ISO standard 9126 is not well accepted.

## 155 - DLR Software Engineering Guidelines

Schlauch, Tobias;  Meinel, Michael;  Haupt, Carina

<https://zenodo.org/record/1344612#.YmvBiHXMKKM>

| Paper_id | Name | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer | Comment |
| :------: | :--: | :--------: | :----------------------: | :------------: | :------: | :-----: |
|   155    |      |            |                          |                | VL       |         |

**Quality Model** ("is based on", "mentions", "defines"): Own metrics. Points 5, 6, 7 and 8 below.

Note: there are no really defined criteria but one can probably extract interesting data from the
recommendations made.

Classification of softwares:

* application class 0: personal use, small scope No real distribution internal or external DLR.
* application class 1: external contribution and use. Software used beyond personal puposes. Need to
  be traceable and reproducible.
* application class 2: need to ensure long-term developpement and maintenability. Need appropriate
  software architecture.
* application class 3: essential to avoid errors and reduce risks. Critical software.

A decision tree (see article) help the software responsible to choose the right application class
with criteria :

* risks for the facility
* scope (large or not)
* distribution of the software
* period for further development (long-term ?)

1. about qualification: be sure that persons involved have the necessary knowledge and training.
2. about requirements management: well documented the functional requirements, the quality
   requirements and the constraints.
3. about software architecture: well documented the architecture in a comprehension manner for the
   group, testability of the software is addressed, architectural concepts and decisions can be
   traced to requirements, key architectural concepts are checked (for example POC), systematic
   review of the software is carried out to find out whether it meets the specified requirements.
4. about change management: how performing changes to software in a systematic and comprehensive
   way: requirements, bugs, optimisations. Often used of web-based ticket systems. Need to preserve
   the results of the development work in a safe and comprehensible way: use of version control
   system. Change process coordinated and documented. How to contribute is documented and
   documentation accessible.
5. about design and implementation: common rules regarding the programming style, use of design
   patterns, documentation of design principles. Modular structure of the software as independent as
   possible. Test of each module. Implementation reflects the software architecture. Automatic check
   of simple rules. No duplication between comments and source code. Avoid complex solutions and
   implementation.
6. about software test: implementation of a tes startegy which may have consequences over the
   software architecture. Different types of tests : module tests (unit tests), integration tests
   (about interactions between components), system tests (global), acceptance tests (customer's
   point of view). Importance of test automation. Necessity to select and systematically evaluate
   metrics.
7. about release management: define the process of publishing a release.licensing conditions must be
   defined. Unique release number. Contains the documentation.
8. about automation and dependency management: software development is complex. Often required
   several software package with a specific version (dependencies) and other programs (development
   environment). Necessity to automate the build process, the execution of tests, the creation of
   the release package.
