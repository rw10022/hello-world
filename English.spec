
namespace lang.English domain

    'Base vocabulary for the english language.'
;

// Declaration of concepts

insert

// Language

        /eng as Eng,
        
// Archetypes

        Eng/entity as Entity,
        Eng/relation as Relation,
        Eng/property as Property,
        Eng/attribute as Attribute,
        Eng/identity as Identity,

// Relations

        Relation/member_of as MemberOf,
        Relation/has_member as HasMember,

        Relation/property_of as PropertyOf,
        Relation/has_property as HasProperty,

        Relation/attribute_of as AttributeOf,
        Relation/has_attribute as HasAttribute,

        Relation/identity_of as IdentityOf,
        Relation/has_identity as HasIdentity,

        Relation/inverse as Inverse,

        Relation/gcl_validates as GCLValidates,

// Properties

        Property/mime as pMIME,
        pMIME/text as pText,
        pMIME/image as pImage,
        pMIME/application as pApplication,

        pText/plain as pTextPlain,
        pText/csv as pTextCSV,

        pApplication/x-sdp as pXsdp,

        pXsdp/bool as pBool,
        pXsdp/int32 as pInt32,
        pXsdp/float as pFloat,
        pXsdp/string as pString,
        pXsdp/date as pDate,

// Attributes

        Attribute/descriptive as aDescriptive,

        aDescriptive/definition as aDefinition,
        aDescriptive/description as aDescription,
        aDescriptive/intention as aIntention,
        aDescriptive/example as aExample,
        aDescriptive/constraint as aConstraint,

        aExample:1 as aExample1,
        aExample:2 as aExample2,
        aExample:3 as aExample3,

        aConstraint:1 as aConstraint1,
        aConstraint:2 as aConstraint2,
        aConstraint:3 as aConstraint3,
        aConstraint:4 as aConstraint4,
        aConstraint:5 as aConstraint5,

        Attribute/dsl as aDSL,
        aDSL:gcl as aGCL,

// Associations

        {Attribute HasProperty pTextPlain},

        // The following associations makes the Subject the one 
        // to be used by the database and not the Object.

        {HasMember Inverse MemberOf},
        {HasProperty Inverse PropertyOf},
        {HasAttribute Inverse AttributeOf},
        {HasIdentity Inverse IdentityOf}

;

// Definition of concepts

insert

// Eng

        {Eng HasAttribute aDefinition}
            = 'the set of all english language concepts',

        {Eng HasAttribute aIntention}
            = 'serves as the root for the archetypes',

        {Eng HasAttribute aDescription}
            = `the language is expressed as a 3-letter code taken 
              `from the ISO-639-3 International standard
            ,

// Entity

        {Entity HasAttribute aDefinition} 
            = 'the set of all things',

        {Entity HasAttribute aIntention}
            = 'serves as the root archetype for all substantial and unsubstantial things',

        {Entity HasAttribute aDescription}
            = `an entity name, as declared under this archetype, provides a textual 
              `representation for a given thing. It is like a pointer to it.
              `An entity can represent concrete or abstract things.
              `It is strongly suggested to annotate a new entity with a definition,
              `an intention, a description and any constraints using the Graph
              `Constraint Language (GCL)
            ,

// Relation

        {Relation HasAttribute aDefinition} 
            = 'the set of all relations',

        {Relation HasAttribute aIntention}
            = 'serves as the root archetype for binary relations among things',

        {Relation HasAttribute aDescription}
            = `an relation name, as declared under this archetype, provides a textual 
              `representation of a relation that occurs between two things. It is
              `used to bind entities, properties, attributes and identities together.
              `It is strongly suggested to annotate a new relation with a definition,
              `an intention, a description and any constraints using the Graph
              `Constraint Language (GCL)
            ,

// Property

        {Property HasAttribute aDefinition} 
            = 'the set of all properties',

// Attribute

        {Attribute HasAttribute aDefinition} 
            = 'the set of all attributes',

// Identity

        {Identity HasAttribute aDefinition} 
            = 'the set of all identities',


// HasMember

        {HasMember HasAttribute aDefinition} 
            = 'enables the associations between groups and their elements',

// HasProperty

        {HasProperty HasAttribute aDefinition} 
            = 'enables the associations between a concept and its properties',

// HasAttribute

        {HasAttribute HasAttribute aDefinition} 
            = 'enables the associations between a concept and its attributes',

// HasIdentity

        {HasIdentity HasAttribute aDefinition} 
            = 'enables the associations between objects and their identities',

// GCLValidates

        {GCLValidates HasAttribute aDefinition} 
            = 'associates a graph constraint to one or more constraints descriptions',

// pText

        {pText HasAttribute aDefinition} 
            = 'the set of all text MIME types (rfc2045)',

// pTextPlain

        {pTextPlain HasAttribute aDefinition} 
            = 'the MIME type text/plain (rfc2045)',

// pTextCSV

        {pTextCSV HasAttribute aDefinition}
            = 'the MIME type text/csv (rfc2045)',

// aDescriptive 

        {aDescriptive HasAttribute aDefinition}
            = 'a descriptive sentence that conveys one or more ideas',

// aDefinition

        {aDefinition HasAttribute aDefinition}
            = 'a concise explanation of the meaning of a concept',

        {aDefinition HasAttribute aIntention}
            = 'is intented to appear in a glossary',

// aDescription

        {aDescription HasAttribute aDefinition}
            = 'a detailed explanation of the meaning of the concept',

// aIntention

        {aIntention HasAttribute aDefinition}
            = 'identifies a purpose or goal',

// aExample

        {aExample HasAttribute aDefinition}
            = 'that which serves as an illustration',

// aConstraint

        {aConstraint HasAttribute aDefinition}
            = 'identifies a restriction or limit on the use of a concept',

        {aConstraint HasAttribute aDescription}
            = 'can be used in "positive way" to cancel-out a previous constraint',

// aDSL

        {aDSL HasAttribute aDefinition}
            = 'the set of all Domain Specific Languages (DSL)',

// aGCL

        {aGCL HasAttribute aDefinition}
            = 'Graph Constraint Language - restricts graph elements and their relations'

;

// Constraints or connectivity rules

insert

// Eng 

        {Eng HasAttribute aConstraint1}
            = 'cannot be instantiated',
    
        {Eng HasAttribute aGCL} = 'this abstract;',

        {{Eng HasAttribute aGCL} GCLValidates {Eng HasAttribute aConstraint1}},

// HasAttribute

        {HasAttribute HasAttribute aConstraint1}
            = 'cannot be instantiated',
    
        {HasAttribute HasAttribute aConstraint2}
            = 'can only have an attribute as the object',

        {HasAttribute HasAttribute aGCL} 
            = 'this abstract;' +
              'allow {/eng (any) this (abstract) /eng/attribute (any)};',

        {{HasAttribute HasAttribute aGCL} GCLValidates {HasAttribute HasAttribute aConstraint1}},
        {{HasAttribute HasAttribute aGCL} GCLValidates {HasAttribute HasAttribute aConstraint2}},

// HasProperty

        {HasProperty HasAttribute aConstraint1}
            = 'cannot be instantiated',
    
        {HasProperty HasAttribute aConstraint2}
            = 'can only have a property as the object',

        {HasProperty HasAttribute aGCL} 
            = 'this abstract;' +
              'allow {/eng (any) this (abstract) /eng/property (any)};',

        {{HasProperty HasAttribute aGCL} GCLValidates {HasProperty HasAttribute aConstraint1}},
        {{HasProperty HasAttribute aGCL} GCLValidates {HasProperty HasAttribute aConstraint2}},

// HasIdentity

        {HasIdentity HasAttribute aConstraint1}
            = 'cannot be instantiated',
    
        {HasIdentity HasAttribute aConstraint2}
            = 'can only have an identity as the object',

        {HasIdentity HasAttribute aGCL} 
            = 'this abstract;' +
              'allow {/eng (any) this (abstract) /eng/identity (any)};',

        {{HasIdentity HasAttribute aGCL} GCLValidates {HasIdentity HasAttribute aConstraint1}},
        {{HasIdentity HasAttribute aGCL} GCLValidates {HasIdentity HasAttribute aConstraint2}},
 
// GCLValidates

        {GCLValidates HasAttribute aConstraint1} 
            = 'cannot be specialized',

        {GCLValidates HasAttribute aConstraint2} 
            = 'cannot be instanciated',

        {GCLValidates HasAttribute aConstraint3} 
            = 'binds a single GCL rule association as subjet to  one or more constraint associations as objects',

        {GCLValidates HasAttribute aGCL} 
            = 'this exact;' +
              'allow {' +
              ' {/eng (any) /eng/relation/has_attribute (exact) /eng/attribute/dsl:gcl (exact)}' +
              ' this (exact)' + 
              ' {/eng (any) /eng/relation/has_attribute (exact) /eng/attribute/descriptive/constraint (final)}' +
              '};',

        {{GCLValidates HasAttribute aGCL} GCLValidates {GCLValidates HasAttribute aConstraint1}},
        {{GCLValidates HasAttribute aGCL} GCLValidates {GCLValidates HasAttribute aConstraint2}},
        {{GCLValidates HasAttribute aGCL} GCLValidates {GCLValidates HasAttribute aConstraint3}},

// pTextPlain
//        {pTextPlain HasAttribute aConstraint1}
//            = 'relaxing parent constraints to no constraints',
//        {pTextPlain HasAttribute aGCL} = 'this any;',
//        {{pTextPlain HasAttribute aGCL} GCLValidates {pTextPlain HasAttribute aConstraint1}},

// pInt32
//        {pInt32 HasAttribute aConstraint1}
//            = 'relaxing parent constraints to no constraints',
//        {pInt32 HasAttribute aGCL} = 'this any;',
//        {{pInt32 HasAttribute aGCL} GCLValidates {pInt32 HasAttribute aConstraint1}},

// pFloat
//        {pFloat HasAttribute aConstraint1}
//            = 'relaxing parent constraints to no constraints',
//        {pFloat HasAttribute aGCL} = 'this any;',
//        {{pFloat HasAttribute aGCL} GCLValidates {pFloat HasAttribute aConstraint1}},

// pString
//        {pString HasAttribute aConstraint1}
//            = 'relaxing parent constraints to no constraints',
//        {pString HasAttribute aGCL} = 'this any;',
//        {{pString HasAttribute aGCL} GCLValidates {pString HasAttribute aConstraint1}},

// pDate
//        {pDate HasAttribute aConstraint1}
//            = 'relaxing parent constraints to no constraints',
//        {pDate HasAttribute aGCL} = 'this any;',
//        {{pDate HasAttribute aGCL} GCLValidates {pDate HasAttribute aConstraint1}},

// pBool
//        {pBool HasAttribute aConstraint1}
//            = 'relaxing parent constraints to no constraints',
//        {pBool HasAttribute aGCL} = 'this any;',
//        {{pBool HasAttribute aGCL} GCLValidates {pBool HasAttribute aConstraint1}},


// aDefinition

        {aDefinition HasAttribute aConstraint1}
            = 'cannot be specialized',

        {aDefinition HasAttribute aConstraint2}
            = 'cannot be instantiated',

        {aDefinition HasAttribute aGCL} = 'this exact;',

        {{aDefinition HasAttribute aGCL} GCLValidates {aDefinition HasAttribute aConstraint1}},
        {{aDefinition HasAttribute aGCL} GCLValidates {aDefinition HasAttribute aConstraint2}},

// aDescription

        {aDescription HasAttribute aConstraint1}
            = 'cannot be specialized',

        {aDescription HasAttribute aConstraint2}
            = 'cannot be instantiated',

        {aDescription HasAttribute aGCL} = 'this exact;',

        {{aDescription HasAttribute aGCL} GCLValidates {aDescription HasAttribute aConstraint1}},
        {{aDescription HasAttribute aGCL} GCLValidates {aDescription HasAttribute aConstraint2}},

// aIntention

        {aIntention HasAttribute aConstraint1}
            = 'cannot be specialized',

        {aIntention HasAttribute aConstraint2}
            = 'cannot be instantiated',

        {aIntention HasAttribute aGCL} = 'this exact;',

        {{aIntention HasAttribute aGCL} GCLValidates {aIntention HasAttribute aConstraint1}},
        {{aIntention HasAttribute aGCL} GCLValidates {aIntention HasAttribute aConstraint2}},

// aExample

        {aExample HasAttribute aConstraint1}
            = 'cannot be specialized',

        {aExample HasAttribute aGCL} = 'this final;',

        {{aExample HasAttribute aGCL} GCLValidates {aExample HasAttribute aConstraint1}},

// aConstraint

        {aConstraint HasAttribute aConstraint1}
            = 'cannot be specialized',

        {aConstraint HasAttribute aGCL} = 'this final;',

        {{aConstraint HasAttribute aGCL} GCLValidates {aConstraint HasAttribute aConstraint1}},

 // aDSL

        {aDSL HasAttribute aConstraint1}
            = 'cannot be specialized',

        {aDSL HasAttribute aGCL} = 'this final;',

        {{aDSL HasAttribute aGCL} GCLValidates {aDSL HasAttribute aConstraint1}},

// aGCL

        {aGCL HasAttribute aConstraint1} 
            = 'can be applied to any symbol using the has_attribute relation',

        {aGCL HasAttribute aGCL}
            = 'allow {/eng (any) /eng/relation/has_attribute (exact) this (exact)};',

        {{aGCL HasAttribute aGCL} GCLValidates {aGCL HasAttribute aConstraint1}}

;
