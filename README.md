# EcloudFinance-module
Education-cloud finance module is a software as a service(SaaS) that runs on cloud server online. In most cases, web browsers are used to access it over the network such as the internet. Most education institutions have been facing a challenge in managing and accounting for the funds and resources in Kenya. Education-cloud finance module will allow these institutions to manage and account for the funds and resources. This software will be deployed on the cloud servers to ease its access to any subscribed institution. Institutions will be able to enroll themselves in the service offered by this software. It will not be taking users(institutions) storage as it will not be a requirement to install the software in their local machines but rather it will be storing data in the cloud servers. The service will be accessed using the browsers over the internet.  Education-cloud finance module will be developed using django the python framework.


# The full project proposal

MASENO UNIVERSITY
SCHOOL OF COMPUTING AND INFORMATICS
DEPARTMENT OF INFORMATION TECHNOLOGY
CIT 413: INDIVIDUAL  PROJECT


Abbreviations:
SaaS- Software as a Service
AWS- Amazon Web Services
GCP- Google Cloud platform
ERP- Enterprise Resource Planning
OWASP- Open Web Application Security Project. 
S3- secure Simple Storage.




Table of Contents
DECLARATION	2
ABSTRACT	3
Abbreviations:	4
Chapter 1	7
1.1 Background	7
1.2 PROBLEM STATEMENT	8
1.3 MAIN OBJECTIVE	8
1.4 Specific Objectives	8
1.5 Research questions	9
1.6 Scope and Limitations	9
1.7 Justification	10
Chapter 2	11
LITERATURE REVIEW	11
2.1 Introduction.	11
2.2 Existing systems/software's as a service.	12
2.2.1 Skolaro	12
2.2.2 ShulePro	14
2.3 Proposed system/SaaS.	17
Education-cloud Finance Module.	17
Review of relevant articles and publications	17
2.4 Conclusions	18
Chapter 3	20
METHODOLOGIES:	20
3.1 Introduction:	20
3.2 Software development methodologies.	20
3.2.1 Agile development methodology	20
3.3 Research approach	20
3.4 Data collection	21
3.5 Sampling	21
3.6 Review of various literature's.	22
3.7 Requirements	22
3.7.1 Hardware requirements	22
3.7.2 Software requirements	22
3.7.3 Non-Functional Requirements	23
a) Usability​​:	23
b) Compatibility​​:	23
c) Security​​:	23
d) Performance:	24
3.7.4 Functional requirements	24
1. Homepage	24
1 & 2. Login and registration	24
3. It is possible to recover forgotten passwords using e-mail addresses	25
Chapter 4:	26
SYSTEM DESIGN	26
4.1 Database Design and Normalization	26
4.2 System Design (Logical Design)	26
 4.2.1 Data Flow Diagram	26
4.2.2 Use case diagram.	27
4.2.3 Entity relation diagram.	28
4.3 System Testing and Evaluation	29
4.3.1 Test 1: Views	29
4.3.2 Test 2: Models	29
4.3.3 Test 3: Forms	29
4.3.4 Test 4: financial management	30
References	31

Chapter 1
1.1 Background
Currently the number of organizations has increased rapidly with the need to make profits and interests. Among these organizations is institutions that offers education as a service. To run these institutions the key component that is required is funds. Funds fall under the finance docket  of any organization. Therefore without finance running the institution is not easy. Again the funds and or finance might be there but managing it becomes a big problem here.  Embezzlement of funds and loss of the same has been recently reported in many organizations. Especially knowing that the era of corruption tends to have taken control of this docket. This has led to poor utilization of resources or overspending the funds on things that are not necessary, leaving  others unattended thus non-uniform development taking place due to localization of resources.

This country, Kenya, being in its move to technological development, most organizations has not fully adopted the computerized systems for managing the funds. Not just the computerized systems, also they are still stuck on the physical servers which are expensive to acquire and maintain. The institutions tend to dwell on the paperwork. They should eliminate these platforms/physical servers and emulate the cloud computing aspects offered, SaaS. This will lower the cost of acquiring these servers.

For easier management of funds or any other aspect that needs management, a centralized one0ff command center is very much necessary . Currently most institutions has their finance management systems which do not relate to any other, it  would save on cost of spending on this if there exists one software that would be common among these institutions. And the best to suit this would be a software as a service that any school would access for use, that is employing the cloud computing aspects.

The problem is on how to manage these funds. Management comes with planning put in place. Planning is well made with the future predictions. This event of planning can be a bit challenging especially with the current paperwork system. To ease this machine learning would help this one out. 

1.2 PROBLEM STATEMENT

In Kenya educational institutions face a challenge in management and accounting for the funds and resources.

1.3 MAIN OBJECTIVE
Build a computerized  cloud based  financial management  module that will run on the ERP. This module will help in management of school funds and other financial related resources. It will also help in keeping track of the resource utilization, and also store data related to this for future reference and planning.  Also will replace the hectic paper work used for the same purpose and ease the retrieval of needed data. The monitoring of how resources are used by these schools by the government will also be easy and quick.

1.4 Specific Objectives
    1. Gather and analyze user and system requirements. 
    2. Create the module’s user interface to allow users/client interact/use  this financial management module.
    3. Create the database for this module that will allow clients which is schools involved to store their financial data.
    4. Enable the data science and machine learning capabilities to this module for the analysis and prediction of financial status to allow for planning and management of these funds.
    5. Test and validate the module.
    6. Deploy the module to a cloud server(AWS, GCP, Azure).

1.5 Research questions
    1. How do schools interact with the current financial management module.
    2. How is the financial data stored in the current financial systems.
    3. How is analysis and prediction of financial status done in the current system.
    4. How is the current financial system module deployed.

1.6 Scope and Limitations
The project will cover the financial aspects of schools. It will help in planning aided by the data science and machine learning capabilities enabled. However, the this project has a lot of limitations: these are, lack of funding to accomplish the mission targeted by it, Initial cost of hosting the module is high and also not available, for one to access this cloud based module it means that you have internet connectivity which is not well distributed in all places, you also need electric power, which again, more marginalized areas will face as a problem and also lack of computers in the place as the schools cannot afford this, the main problem at this, is lacking skilled person to work with this module as most are teachers they may require system admin skills, and be at least computer literate.

1.7 Justification
Currently, most schools have fully embraced the paper work operations, to acquire these papers on daily basis is expensive plus other required resources like printers, physical servers among others, this module is replacing the paperwork with the computerized system, also in the place of physical servers this will be replaced   by cloud computing servers. The cost of managing these financial operations is also expensive as many applications will be developed, but with this module, it will have the capabilities to serve all schools/institutions. And this time round,  prediction of financial status will be automated by the machine learning and data science in place, thus easing the planning of how to utilize resources.
Chapter 2
LITERATURE REVIEW
2.1 Introduction.
(https://www.oracle.com/applications/erp/what-is-financial-management-system/)Finance being the most important branch of an organization, needs to be highly monitored as it can lead to the fall of an organization. This draws the attention to find mechanism to monitor this. The education domain being the subject of concern here, there needs to be a way to manage the financial aspects of this domain. To run any education institution, funds plays the main role here.

In the recent past, (Financial Management Information Systems (FMIS),Jan 07, 2020)most institutions has been managing their funds poorly due to lack of a computerized system for this purpose. They have been dwelling on paperwork mechanisms which are hard to track, retrieve and maintain, thus drawing the need to have a computerized mechanisms or platforms for this purpose.
Formerly, there has been few systems that manages the funds for education institutions. Some of these systems were depended on in the non-technological era such as typewrites. Due to unreliable instances of these systems more advanced and considered as technological were introduced, the use of smart phones, laptops an desktop computers. Due to the challenges that came with the introduction of these high tech devices for accessing data and websites, a highly advanced platform was developed. This platform needs to be run as a cloud computing service and offered as software as a service.
(Oracle’s Modern Software and Solutions for Financial Management Systems,https://www.oracle.com/applications/erp)Computerized devices usage has increased over the years due to their affordability. These devices has become the platform that supports many desktop and mobile applications. These applications will be the software offered as SaaS(Cloud Considerations for a Modern Finance Management Solution
,https://www.oracle.com/applications/erp) and will be the most favorable solution to the existing problem of lacking a computerized system that runs on the ERP to manage the schools funds and resources(Reports Needed from an ERP System,https://www.oracle.com/applications/erp).
This chapter discusses the relevant researches that had been done before by researchers. Moreover, it also discusses the existing systems that is applications that have been developed before and the proposed system. In addition, it will discuss the capabilities of the proposed system and the loop holes it will cover from the existing systems.
2.2 Existing systems/software's as a service.
2.2.1 Skolaro


Skolaro financial management software designed for the education market for providing a comprehensive overview of schools and college finances enables an institute to set-up a perfect fee management functions with accurate ledger structure with input ledger entries with an easy intuitive interface, making the whole process error free and fast. All kinds of fees are recorded and reflected in one place ready for reference. Also deals with the complexities of found accounting and financial reporting, has everything an institution business manager needs to operate efficiently. Its a globally used platform and cloud based application that was developed in India back in 2010.
Disadvantages
It does not separate concerns, that is it has many functionalities docked together. These are fee management, Accounting and payroll management. Payroll management system should be out of this scope. That is should be managed by the employer of teachers but not managed by the school managements.
2.2.2 ShulePro





As from the screenshots, its clear that shulepro does a lot of management of various school activities, that ranges from the timetables, assignment of learning venues among-st others.  It also has the general management of the school like sharing of the school resources like printers. It was developed in Kenya, it won the best windows school management system in 2016 connected summit.
Disadvantage
It does not separate  concerns, that is, should be a wholesome system managing only one feature of management, which it should it well and to its best levels. It is only suited for windows users. It requires a user to install it into their systems so that they can use it.
2.3 Proposed system/SaaS. 
Education-cloud Finance  Module.
Education-cloud Finance  Module, is a finance module learning on the ERP. It manages only the finance aspect of the education institutions. It does not manage other resources of the schools, like timetables, learning venues, payroll management and teacher’s leave issues. As it would be the best practice of software development it separates concerns, as it only focuses on one issue only. This system will have the capabilities to  manage all the schools funds as it will be offered as SaaS, meaning that all schools will be able to access it from their schools  because its a service.  It will be hosted on the cloud platform. This will help in reducing the cost of buying extra  hardware like physical servers for the storage purposes, it will have the capabilities to use either s3 or Google Big-query databases which are offered on the cloud. Also it being a cloud service it means you access it at any given time when you need it without limitations. This will also ease the tracking of school’s funds by the government as it will be centralized, using one common database. And using the newest technologies of distributed and centralized systems will make it easier and cost saving for the schools.
Review of relevant articles and publications
    i. Financial institutions management: Risk management approach
Financial institutions management, risk approach(Cornett, M. M., & Saunders, A. 2003 Financial institutions management:). Institutions must rethink their risk management strategy on funds and adopt a holistic approach to reduce liabilities while improving effectiveness. In this same approach, educational institutions should adopt thee strategies in order to manage their resources effectively. It could be the only reliable way to run the entire institution.

       ii. Financial accountability. The principal or the school governing body?
       (Mestry, R. 2004)The Schools Act 84 of 1996 prescribes how a school should manage its funds. It also provides guidelines for the school governing body and the principal on their roles and responsibilities in managing the finances of the school. However, there are school governing bodies and principals that have little knowledge of the contents of the Schools Act or are simply interpreting it incorrectly and this has led to many schools being victims of mismanagement or misappropriation of funds in the form of embezzlement, fraud and theft. Although the Department of Education provides training for school governing bodies in financial management, financial problems in many schools have not abated. With this in mind, a well structured system needs to be put in place to monitor how funds are managed. A well tracking methodology needs to be put in place for accountability purposes.
2.4 Conclusions
As seen from all the existing systems is that they are not separating concerns, They are managing a lot of stuffs and resources in the institutions. From the best practices of software development and design, 12-Factor app to be precise, separation of concerns is the best. The proposed system will obey and follow all the underlying rules of software development as stated by 12-factor app and django python framework for software development. The system will only concentrate with the finance module of the ERP, to help in managing the funds disbursed to schools by the government and other funds the schools earns from its businesses.  The module will run on the cloud as a service making it cheap, and easy to manage by the involved schools. It will also have a common database for all the schools thus cost saving on extra and additional hardware for the storage purposes. And as strongly supported by the reviewed literature's and publications, its therefore clear that a  system to manage finance needs to be put in place. The risk management approach, for the continuity of an institution there will be need to adopt a holistic way to cub out liabilities. To enhance accounting on how funds have been used a system for keeping records and tracking of documents is also needed.
Chapter 3
METHODOLOGIES:
3.1 Introduction:
This chapter will cover the detailed explanation of methodology that is being used to make this project complete and working well. The method used to achieve the objective of the project will accomplish perfect results. In order to evaluate this project, the methodology will be based on System Development Life Cycle (SDLC), which consists of three major steps: planning, implementing and analysis. But on this chapter, we focus mainly on planning. The planning phase entails data collection and hardware and software requirements gathering.
3.2 Software development methodologies.
3.2.1 Agile development methodology
This being the best and world widely used development methodology for software development I decided to go with this approach specifically going for Kanban. (Daniel-Roy-Greenfeld-Audrey-Roy-Greenfeld-Two-Scoops-of-Django2015) Kanban makes it easier to deliver a well developed software as involves small iterations. Over this iteration usability can be tested and with it logical errors will be minimal. 
3.3 Research approach
The research approach is the conceptual structure in which a research is carried on. For this
purpose, a research approach has to be chosen between several types of research: descriptive or analytical, applied or fundamental, qualitative or quantitative, conceptual or empirical, among others. (R., 2004) Applied research aims at finding a solution to a concrete problem that society or an industry is facing. Whereas, the fundamental research approach
is tailored for formulating theories and generalizations. Typically, fundamental research is used for mathematical problems in order to prove that a hypothesis is false or no longer correct due to different factors. This thesis addressed several research questions aiming at finding a solution to a concrete and identified issue in the ICT domain. Hence, it is catered  for the applied research approach.
This research intends to find a solution to the issue of deciding which software development strategy is best for a specific project. For this purpose, we conduct an analysis of the literature and a survey that both provide past and current information about the subject.
3.4 Data collection
Data is an asset that can be used to evaluate the value of any existing element or any system to our case. The value is determined when this data is analyzed and presented. Therefore, data collection is a crucial phase for any development and cannot be skipped. There are many ways through which data can be collected. This drives us to a research  methodology to determine the main method to compile the most reliable data, that is by getting the best sources of the data. These methods may Include; sampling, questionnaires, reviewing literature's. 
3.5 Sampling
After sampling the existing systems, all have shown almost the same defects, that is lack of separation of concerns. From this lets the developer to gather information that the system to be designed and developed should utmost separate concerns. From the data collected from these existing systems, it will be possible to develop a more suitable system that obeys all the rules of software development and a better than existing ones in the sense that it will have separation of concerns, that is will only deal with the finance module but not the ERP system as the whole. Also from the visited systems,(existing) no one is running on a cloud platform, no one has a common database for all schools. This aids in knowing what the system is lacking and in this system(proposed) all these will be put into consideration.
3.6 Review of various literature's.

3.7 Requirements
3.7.1 Hardware requirements
 Dual-core 64-bit processor.
 Core i3 and above clocked at nearly 2GHz (but for big apps one needs a better processor like core i5)
 4 GB of RAM and above.
 Up to 24GB of internal storage ( plus ample space multiple projects).
  Linux(Ubuntu) or windows 10.
3.7.2 Software requirements
 Cloud computing service (AWS,GCP, AZURE)
    Virtual Machine instances (3.75 GB RAM, 23GB ssd storage.)
    Python 3.0 and above.
    Django 2.2 and above plus its prerequisites
   
     Django-rest-framework
     Oauth2 provider
    Vs-code

3.7.3 Non-Functional Requirements
A Non-functional requirement is a requirement that specifies criteria that can be used to judge the
operation of a system, rather than specific behaviors. Broadly, functional requirements define what a system is supposed to do and non- functional requirements define how a system is supposed to be. Non-functional requirements are often called "quality attributes" of a system.
a) Usability​​:
Testing the usability is a measure of how easily the system can be used by end users and time
required to get used to using the application. It entails assessment of the user's attitude towards
using the application. A usability test ensures ease of use, ease of Learning or familiarizing with the
system and satisfaction of the user with the entire experience.
b) Compatibility​​:
Testing the compatibility is a non-functional testing technique conducted on the software to
evaluate the software's compatibility within different environments. It is performed to ensure that
despite the differences in size, resolution, screen and version of computerized devices, the software
should work as desired. Device compatibility testing refers to validating whether the under-test
software can work well on different  devices with various platforms, appliances and features.
c) Security​​:
Testing the Security is a testing technique to determine if an information system protects data and
maintains functionality as intended. Testing data can be processed as different combination of
usernames and passwords and its purpose is to check that only the authorized people are able to
access the application. Security is a set of measures to protect an application against unforeseen
actions that cause it to stop functioning or being exploited. Security testing ensures, that system or
application, is free from any loopholes that may cause a big loss. The goal of security testing is to
identify the threats in the system and measure its potential vulnerabilities. Oauth2 and OWASP  will take charge at this point.
d) Performance:
Testing the Performance is a technique used to determine responsiveness and stability of the system parameters under various workload. Performance testing measures the quality attributes of the system such as scalability, reliability and resource usage. Performance testing is mainly used to ensure that its response time doesn’t lower under peak load conditions, to ensure that the application performs in the same way in different versions and ensure that the software will work efficiently at different bandwidths.

3.7.4 Functional requirements
1. Homepage
FQ01: On the first launch of the software, the user is presented with several text and graphics
that allow him/her to better know and understand the idea behind the system.
1 & 2. Login and registration
FQ02: Users/clients/Institutions/Schools can register and login using either an E-mail address or Username.
FQ03: Registration requires adding Institutions details including: name, email address, password, contact details, location etc. It is also possible to display the entered password to verify if it is correct.
Logging in is not required to use the software, but some functionalities may not be available for users who are not logged in.
3. It is possible to recover forgotten passwords using e-mail addresses
FQ04: The client enters their email address and an e-mail is sent with a reset password link. The link is prepared to be handled by the system. After opening the link, the application is opened on the screen for setting up the new password. After setting up a new password, the client stays logged in.
Chapter 4:
SYSTEM DESIGN
This chapter provides a conceptual view of the proposed system and its functionality. This design
stage takes the initial input requirements that were identified in the approved requirements
specification document. For each requirement, there is a set of one or more design elements that
are produced using the different prototypes. These design elements describe the desired software
features, in detail, including functional hierarchy diagrams, screen layouts, activity diagrams, and
class diagrams. The intention of these diagrams is to describe the software in detail so that the
system developer can develop the application with less additional design input.
4.1 Database Design and Normalization
Normalization is one of the database design technique that divides larger tables to smaller tables
and links them using relationships. Here is a design of relationships of the proposed system.

4.2 System Design (Logical Design)
        4.2.1 Data Flow Diagram
                                                                                 Management of db                                                                                                                                   
                                                                                                             Software and site management.                                                                                                                                 
                                                                 storage of school’s finance details
                   
                          enrollment and login                                                                                                                                         
                      school’s finance details   
4.2.2 Use case diagram.
The proposed software has two main users, that is subscribed school’s. The store their financial details, manipulate it and print out reports. The second user is the administrator. The admin manages the software and the database as whole.
                              






                Administrator                                                                                                     











     institution finance 
     department.
4.2.3 Entity relation diagram.












4.3 System Testing and Evaluation
This section will briefly describe how its planned to test the effectiveness and usability of the fully
developed software by the user and to also ascertain that the problem underlying is being solved by this project.
4.3.1 Test 1: Views
This involves testing the user interface. All the visible components are tested to ensure that they are responsive to the user interactions.  Also this tests that all the links and paths given point to the correct components. Testing the home page that it is using the rigt templates and points to the right static folders.
4.3.2 Test 2: Models
This involves testing the database. The purpose for the database is to store user information. Dummy data is fed into the database to ensure that data is being store, or through the creation of model mommy for testing purposes. Also the database is tested if it can provide the user with stored information.
4.3.3 Test 3: Forms
Forms plays a major role in any given system that involves registration of new users and retrieving user data from any storage sites like databases. Major things t be tested in this project are:
POSTING- the forms will be tested if they can post data into the database.
GETTING- the get method will be tested. That is verify if data can be retrieved from the database.
PUT- this is verify if the user information can be  fully updated upon deletion or creation
PATCH – verifying if the additional update done can update user information.

4.3.4 Test 4: financial management
The system will be tested against the objectives to see that the main objective is achieved.

References
Daniel-Roy-Greenfeld-Audrey-Roy-Greenfeld-Two-Scoops-of-Django_-Best-Practices-for-Django-1.8-Two-Scoops-Press-2015
https://www.oracle.com/applications/erp/what-is-financial-management-system/
https://www.worldbank.org/en/topic/governance/brief/financial-management-information-systems-fmis
Cornett, M. M., & Saunders, A. (2003). Financial institutions management: A risk management approach. McGraw-Hill/Irwin.
Mestry, R. (2004). Financial accountability: the principal or the school governing body?
