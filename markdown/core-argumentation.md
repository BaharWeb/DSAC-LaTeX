# PhD Thesis Argumentation Outline

## Introduction

### Situation

Web Systems are widely used and accepted due to their advantages over traditional desktop software

### Problem (Motivation)

Modernization of existing legacy systems is hard due to their characteristics  

### Challenge (Problem Statement)

Companies are struggling to commence Web Migration due to effort and risk and a lack of dedicated approaches for the initial phase, but academia considers this topic solved

### Research Questions

#### Research Question 1

How to support software companies to commence web migration?

#### Research Question 2

How to support commencing web migration with limited effort?

#### Research Question 3

How to address concerns about risk when commencing web migration?

## Problem Analysis

Case Study: Analysis of Situation of concrete ISV SME

### Stakeholder

SME-sized ISVs with legacy, non-web, desktop applications and large existing user bases

#### Implied Characteristics

SME-sized ISV

- Limited resources
- Limited Web Engineering Expertise
- Limited Web Migration Expertise
- Existing Expertise in Legacy Technology

Legacy, non-web, desktop applications 

- Architectural degradation and Technical Debt
- Erosion of soft knowledge
- Valuable knowledge tacit in the source code
- Graphical User Interfaces using heterogenous GUI technologies

Large existing user base

- Contracts for updates and maintenance, strict update cycles
- Ongoing agile development
- Customer impact risk

### Stakeholder Problem

initial hurdle to commence a web migration due to doubts about feasibility and desirability

Identified problems > **Stakeholder Requirements** (C1 Risk, C2 Re-use, C3 Expertise & Tools Support, C4 Agile) 

## State of the Art

Many existing approaches 50/50 MD non-MD in orthogonal groups

Few comprehensive approaches, from large-scale research projects

Web migration is very situation-dependent, best solutions provide methodologies for tailoring processes

### Gaps

- Encapsulation does not create real web applications
- Poor support for initial phase in particular wrt. to risk
- Reuse only for functionality, not for UI/interaction, no tools, no metrics
- High expertise requirements, poor support for SME ISVs
- Stand-alone processes, integration not addressed

## Concept

### Situation
Probleme von ISVs bei Web Migration und Gaps im SotA

### Method
Solution design based on HCD/LFA

### Research and solution design
#### Research objectives
Overarching Goal: support ISV to commence WM with limited resources, lack of WE expertise

RO1: RE to identify and manage existing knowledge in legacy source code with limited resources, lack of WE expertise

RO2: RM to demonstrate feasibility and desirability of web-based version of legacy system with limited resources, lack of WE expertise

RO3: HCI to control impact of WM on customers with limited resources, lack of WE expertise

### AWSM
#### Principles
P1 Open Web Standards ()
P2 Methodology over Process
P3 Model-driven Agnosticism
P4 Rapid Prototyping
#### Formalisms
based on KDM metamodel using extension mechanism

Legacy System (artifacts)
SCKM (assets, mapped to KDM artifacts/areas) defines knowledge, types, annotations, knowledge base
Legacy UI (kdm ui elements + types and bouding boxes) defines components, hierarchy, types, bounding boxes

#### Methods
AWSM:RE für RO2
AWSM:RM für RO3
AWSM:CI für RO4

#### Tools
AWSM Platform

## AWSM:RE

### Situation

Knowledge in LS

### Problem

Not/Poorly documented

### Challenge

How to recover knowledge with limited resource

### Main Research Question

How to apply crowdsourcing paradigm to reverse engineering

## AWSM:RM

### Situation

Doubts about desirability and feasibility

### Problem

Purely technical focus of feasibility studies/migration pilots, no tangible results for communication of plausibility and advantages of web version

### Challenge

How to demonstrate desirability and feasibility with limited resources and lack of WE expertise

### Main Research Question

How to apply rapid prototyping paradigm to web migration

## AWSM:CI

### Situation

Established user base, web migration visibly changes the user interface

Changes impact users (learning effort), consistent look and feel is important, but not addressed by existing approaches, controlling impact means measuring similarity

### Problem

Existing UI similarity approaches cannot be applied to legacy and web UIs because they are based on code analysis

### Challenge

How to control impact through interface changes with limited resources and lack of web engineering expertise

### Main Research Question

How to measure similarity between legacy and web UIs