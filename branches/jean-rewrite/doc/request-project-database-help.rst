Request for help on UNEP Project Database application
=====================================================

The United Nations Environmental Programme (UNEP) has developed a
Project Database application, to keep track of and manage proposed and
running projects. This is a Plone product with Archetypes-based content
types. There are 7 content types now, with 22 schemas shared among them,
numbering some 66 fields in total, and 3 workflows. 

The project does not always follow best practices, and some refactoring
may turn out to be advisable.

They have now completed an internal review which has resulted in a
number of change requests. Types of changes include:

- Addition of functionality. This may involve integration of third-party
  products.
- Adding and editing of page templates for editing and reporting.
- Changes to field labels and field order within templates.
- Editing rights and security needs to be audited. 

An overview of the change requests suggests that the following products
are candidates for integration:

SessionCrumbler
  Requirement: enable timed logout.

mxmWorkgroups (or one of the other workgroup implementations)
  Enable maintenance of site editing rights by way of group membership.

FinanceFields
  Fields implementing proper monetary arithmetic, taking currencies into
  account. Floating point rounding issues are addressed. Widgets are
  provided. This is obtainable from Upfront Systems: contact
  jean@upfrontsystems.co.za

UNEP is looking for a developer to update the schemas in accordance with
a specification document, go through the feedback document formulating
change requests in terms of development tasks and implementing them, and
deliver a working product.

Time is tight: there is about 3 weeks of work to be done by the
beginning of December.

All interested parties should contact Sean Khan <Sean.Khan@unep.org>.

