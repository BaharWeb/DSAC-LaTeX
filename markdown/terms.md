# Terms used
TODO: Use ISO/IEC/IEEE International Standard - Systems and software engineering--Vocabulary

## Web System

> Idea of umbrella term from [@Kienle2014EvolutionWeb], definition adapted from [@Gaedke2000Diss;@Kappel2006WebEngineering]
>
> A Web System is a software system based on technologies and standards of the World Wide Web Consortium (W3C) that provides Web specific resources 

## Web Application

> [@Kappel2006WebEngineering]
>
> A Web Application is a software system based on technologies and standards of the World Wide Web Consortium (W3C) that provides Web specific resources such as content and services through a user interface, the Web browser.

Alternatives:

> Gaedke 2000
>
> Eine Software-Anwendung, die auf Technologien des World Wide Web beruht und deren Implementierung auf Web-spezifischen Ressourcen basiert.

## Legacy System

> Definition Legacy System [@Brodie1995Migrating]
>
> Any system that cannot be modified to adapt to constantly changing business requirements and their failure can have a serious impact on business.

Alternatives:

>  Definition Legacy Information System [@Bisbal1999LegacyInformationSystems]
> Any information system that significantly resists modification and evolution.

## Migration

Superclass of all (replacement, redevelopment, wrapping, transformation)

>  Here we use the term migration when referring to any approach which **moves the entire legacy system** and its **core framework** to the **new environment**. [@Almonaies2010SOAStrategies]

> Migration that moves the system to a **new platform**, while **retaining the original system data and functionalities**. (One of three main modernization techniques)[@Canfora2008, citing Bisbal]
>
> Migration, which moves the LIS to **a more flexible environment**, while **retaining the original system’s data and functionality**. (One of three main LIS Coping strategies) [@Bisbal1999LegacyInformationSystems]

> migration in which a legacy application is gradually moved to SOA **with reusing the legacy components** [@Khadka2013aSurveySOAMigration]

> **During a system's life**, it may have to be **modified to run in different environments**. (Part of maintenance process in software life cycle) [@ISO/IEEE2006SoftwareLifeCycle]

## Independent Software Vendor (ISV)

> A software producer that is not owned or controlled by a hardware manufacturer; a company whose primary function is to distribute software. Hardware manufacturers that distribute software (such as IBM and Unisys) are not ISVs, nor are users (such as banks) that may also sell software products.
> ISVs typically offer products that the primary vendor (i.e., IBM) does not offer, allowing clients of that vendor to round out their software needs. ISVs create price competition and also increase the pace of technology innovation in their markets.

[https://www.gartner.com/it-glossary/isv-independent-software-vendor/]



## Web Migration

## Modernization

All approaches together, including Wrapping, Maintenance??, Migration, Transformation, Redevelopment

## Migration



Im Kontext von Legacysystemen ist die Migration der Vorgang des ¨Ubergangs von einer Implementierungsform in eine andere Implementierungsform. Die Migration betrifft die Umstellung von: • der Einstellung der Menschen, in der Regel der Mitarbeiter, doch kann maninSpezialf¨allen auch von einer Kundenmigration sprechen,
• Prozessen, • Technologien, • Softwaresystemen.
Im Gegensatz zur Maintenance, s. Kap. 7, muss sich jedoch am System
einer der grundlegenden Bestandteile, beispielsweise die Hardware oder die Architektur ver¨andern, damit der Prozess als Migration bezeichnet werden kann. Im Sinne der Entwicklungsbetrachtung sind Migrationen immer revo- lution¨are Ver¨anderungen, welche im Rahmen einer regul¨aren Evolution nicht darstellbar sind. Ein zweites Charakteristikum f¨ur Migration ist der hohe Im- pact, s. Abschn. 7.8, auf einen großen Teil der Legacysoftware, s. Abb. 5.1. F¨ur jede Umstellung eines Legacysystems, sei es der Ersatz durch ein
COTS-Software-System oder eine vollst¨andige Neuentwicklung, wird immer eine Migration ben¨otigt, sogar das Abschalten eines bestehenden Legacysys- tems verlangt nach einer Migration [@Masak2006]

## Reengineering

> Reengineering is defined as the examination and alteration of software to reconstitute it in a new form, and includes the subsequent implementa- tion of the new form. [@SWEBOK2014]

> reengineering 1. examination and alteration of software to reconstitute it in a new form, including the subsequent implementation of the new form [ISO/IEC TR 19759:2016 Software Engineering — Guide to the Software Engineering Body of Knowledge (SWEBOK), 5.4.2] 2. complete cycle of performing reverse engineering followed by forward engineering
> [@ISO/IEEE24765Vocabulary]

> Re-engineering as an approach is generally composed of two components: reverse engineering, and forward engineering. Reverse engineering does not change the system. It provides an alternate view of the system at a different level of abstraction. This generally means redocumenting code as schematics, structure charts, or ßow diagrams to assist in understanding the logic of the code. Additionally, the process offers opportunities for measurement, problem identiÞcation, and the formulation of corrective procedures. Forward engineering is the process of system-building. This process begins with an existing system structure that is the frame- work for changes and enhancements. [@IEEE1219Maintenance]

> Reengineering – Beim Reengineering wird die vorhandene Legacysoftware unter vollständiger Beibehaltung der bestehenden fachlichen Funktionalität neuentwickelt. Das Reengineering kann vollständig oder auch nur partiell sein. [@Masak2006]

cf. General Model for Software Re-engineering [@Byrne1992Reengineering] (Reverse engineering, alteration, forward engineering)





## Software Assets

> asset - a useful or valuable thing or person (Oxford Dictionary of English)

An asset is "a useful or valuable thing" (Oxford Dictionary of English). "A software asset is a description of a partial solution ... or knowledge ... that engineers use to build or modify software products." ([@OMG2011KDM]) Parts of software can be an artifact and an asset at the same time (e.g. documentation). Unless explicitly codified, we consider requirements, models, rules etc. represented by the legacy source code as assets but not artifacts, since they are not tangible.

Examples:

- Models
- Business Rules
- Business Processes

## Software Artifacts

> A software artifact is a tangible machine-readable document created during software development. Examples are requirement specification documents, design documents, source code and executables. (KDM)

> artifact - an object made by a human being (Oxford Dictionary of English)

In this thesis we distinguish between software artifacts and assets. "A software artifact is a tangible machine-readable document created during software development. Examples are requirement specification documents, design documents, source code and executables." ([@OMG2011KDM])

Examples:

- Source code
- Running System (Executable)



## Service

> At the core of an SOA is a service. A service is a coarse-grained, discoverable, and self- contained software entity that interacts with applications and other services through a loosely coupled, often asynchronous, message-based communication model. [@Lewis2005SMART]



## Web Service

>  The most common (but not only) form of SOA implementation is that of web services, in which (1) service inter- faces are described using Web Services Description Language (WSDL), (2) payload is transmitted using Simple Object Access Protocol (SOAP) over Hypertext Transfer Protocol (HTTP), and, optionally, (3) Universal De- scription, Discovery and Integration (UDDI) is used as the directory service. [@Lewis2008SMART]

## SOA Migration

> In many SOA migration projects, the goal is to reengineer the legacy systems into a set of services which can be dynamically selected and are distributed across organization boundaries. [@Razavian2014a]



## Reverse Engineering

> "a software engineering approach that derives a system's design or requirements from its code" [@ISO/IEEE24765Vocabulary]

## Concept [@Rajlich2002Concepts] {#def:concept}

> Concepts are units of human knowledge that can be processed by the human mind (short-term memory) in one instance.

## Crowdsourcing [@Howe2006] {#def:crowdsourcing}

> the act of a company or institution taking a function once performed by employees and outsourcing it to an undefined (and generally large) network of people in the form of an open call.



## Migration Engineer

We will use the term *Migration Engineer* to refer to a Software Engineer who is performing web migration activities. Migration Engineers are to be considered a sub-class of Software Engineers, i.e. all super-class characteristics apply