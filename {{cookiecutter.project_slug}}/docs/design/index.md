# Design

In this section you must have everything related with the design of the product.

Two important type of documents you can find in this matter are ADRs and SRSs.

## ADRs

ADR: _Architecture Decision Record_: It's a document where is specified an
architectural decision of the software.
It can include context from outside the product.

### Example

You develop a very first product, which you are hosting at home,
but you want to take it to the cloud into production.
You will have to answer lots of questions:

- What is the new architecture? Draw the sequential diagram with all the details.
- How am I going to release it? Docker, plain code, library?
- What type of machines am I going to use? Do I have special hardware requirements?
- Does my product needs any load balancers, proxies, etc? How should I program them?
- Etc etc etc.

??? example "ADR Template"

    This is the basic template of an ADR

    ```md
    # ADR-0000 - <!--ADR TITLE-->

    <!--Brief description of the issue been discussed-->

    ## Status

    - **Draft | Proposed | Rejected | Accepted | Deprecated | Superseded**

    ## Decision

    <!--This section MUST describe the adopted decision (solution). It SHOULD stated in full sentences, with active voice.
    Keep in mind that an ADR MUST only contain one decision (specificity).-->

    ## Context

    <!--This section describes the assumptions, concerns and the forces at play, including technological, political, social,
    and project local. These forces are probably in tension, and should be called out as such.-->

    ## Arguments

    <!--This section MUST include the rationale behind the adopted decision.-->

    ## Implications

    The proposed solution requires implementing the following:

    <!--Implication list: All consequences SHOULD be listed here, not just positive ones.-->

    ## Alternatives

    <!--List of alternatives, exposed as viable options that have been taken into consideration. -->

    ## Notes

    <!--Optional section for capturing notes like useful references and issues that the team discusses during the
    socialization process.-->
    ```

## SRS

A _Software Requirements Specification_ (SRS): It's a description of the product,
the feature, or change to be developed.

### Example

One of your customers wants a new feature into your product.
You must know and define exactly what they want and save it somewhere,
so then you have no complains.
You need a document where you define everything
about this new behaviour.

??? example "ADR Template"

    This is the template of an SRS

    ```md
    # SRSXYZ - <!--ADR TITLE-->

    ## Introduction

    <!--Brief description of the issue been discussed-->

    ## Overall description

    <!--Extended description-->

    ## External Interface Requirements

    <!--External Interface Requirements-->

    ## Functional requirements

    <!--Functional requirements-->

    ## Nonfunctional Requirements

    <!--Nonfunctional Requirements-->
    ```
