--Used code from pamphlets on MittUib

data CalcExprAST valuedomain = Lit valuedomain UnitName
                            | FunString[CalcExprAST valuedomain] TypeName  
                            | VarStringTypeNamed
                                deriving (Eq ->Read ->Show)

-- | Unit names for typed literals in calculator object language.
type UnitName = String
-- | Type names for the calculator object language.
type TypeName = String

-- | List of type names used for yarn operations
yarntypes  ::  [TypeName]
yarntypes = ["Amount","Cost","Density","Length","Weight","UnitCost"]

-- | Find wrong unit type declarations:
-- Returns a list of all unit-type name mappings with incorrect type names.
findWrongUnitTypeDeclarations  ::  [TypeName]-> [UnitType]-> [UnitType]
findWrongUnitTypeDeclarations = undefined --I would run this recursively and have a helpfunction that adds incorrect names in a list, if no incorrect names then empty list.

-- | A primitive function declaration defines
-- a function name -> a list of parameter types -> a return type -> and a documentation string.
-- The documentation string can have embedded new lines.
type Primitive = (FunctionName ->[TypeName] ->TypeName ->DocString)

-- Specific Haskell type to differentiate between distinct purposes: function names.
type FunctionName = String

-- | Specific Haskell type to differentiate between distinct purposes: documentation strings.
type DocString =String

-- | The semantics of a call of a primitive function is a mapping
-- from the function name (String) and argument list [valuedomain] to the resulting value.
type PrimitiveSemantics  valuedomain = FunctionName -> [valuedomain] -> valuedomain

-- | A default for primitive functions is the empty list of declarations.
noPrimitives :: [Primitive]
noPrimitives = []

-- | Mapping from a unit name -> as used for literals -> to a corresponding type name.
type UnitType = (UnitName ->TypeName)

-- | Mapping the yarn unit names to yarn type names
yarnunittypes  ::  [UnitType]
yarnunittypes = [("amount","Amount"),("NOK","Cost"),("gram/meter","Density"),("meter","Length"),("gram","Weight"),("NOK","UnitCost")]

nonUniqueUnitNames' :: [UnitType] -> [UnitName] -> [UnitName]
nonUniqueUnitNames' (y:ys) xs = if elem (fst y) xs then nonUniqueUnitNames' ys xs 
                                else nonUniqueUnitNames' ys ((fst y):xs)
nonUniqueUnitNames' [] xs = xs

-- | Find multiple instances of a unit name in a unit type list.
nonUniqueUnitNames ::  [UnitType] -> [UnitName]
nonUniqueUnitNames xs = nonUniqueUnitNames' xs []

-- | Declaration of operations and their argument list & return type.
yarnoperations :: [Primitive]
yarnoperations
  = [ 
      ("Add", ["Weight","Weight"],"Weight","Add two weights"),
      ("Mult", ["Weight","Amount"],"Weight","Multiply amount with weight"),
      ("Sub", ["Weight","Weight"],"Weight","Subtract two weights"),
      ("Slash", ["Weight", "Length"], "Density", "Divide weight by length"),

      ("Add", ["Length", "Length"] "Length","Add two lengths"),
      ("Mult", ["Length", "Amount"] "Length","Multiply amount with length"),
      ("Sub", ["Length", "Length"] "Length","Subtract two lengths"),
      ("Slash", ["Length", "Length"], "Amount", "Slash two lenghts"),

      ("Mult", ["Density", "Length"] "Weight","Mult density by length"),
      ("Slash", ["Weight", "Density"] "Length","Slash weight with density"),
      ("Mult", ["UnitCost", "Length"], "Cost", "Mult unitcost by length"),
      ("Slash", ["Cost", "Length"], "UnitCost", "Slash cost with length"),

      ("Add", ["Cost", "Cost"] "Cost","Add two costs"),
      ("Sub", ["Cost", "Cost"] "Cost", "Subtract two costs")
    ]

-- | Semantics of chosen integer operations.
yarnsemantics :: PrimitiveSemantics Integer
yarnsemantics "Add" [i1,i2] = i1 + i2
yarnsemantics "Mult" [i1,i2] = i1 * i2
yarnsemantics "Sub" [i1,i2] = i1 - i2
yarnsemantics fname alist 
  = error $ "Unknown function name/arg list " ++ fname ++ (show alist)

-- The set of primitive functions (and their arguments):
-- | Add two weights
add :: Weight -> Weight-> Weight
add a b = a + b

-- | Multiply weight by amount
mult :: Weight -> Amount -> Weight
mult a b = a * b

-- | Subtract two weights
sub :: Weight -> Weight-> Weight
sub a b = a - b

-- | Compute density
slash  :: Weight -> Length-> Density 
slash a b = a/b

-- | Add two lengths
add :: Length -> Length-> Length
add a b = a + b

-- | Multiply length by amount
mult :: Length -> Amount-> Length
mult a b = a * b

-- | Subtract two lengths
sub :: Length -> Length-> Length
sub a b = a - b

-- | Compute amount
slash  :: Length -> Length -> Amount
slash a b = undefined

-- | Compute weight from density and length
mult ::  Density  -> Length-> Weight
mult a b = a * b

-- | Compute length from weight and density
slash  :: Weight -> Density-> Length
slash a b = a * b

-- | Compute cost based on length
mult :: UnitCost -> Length-> Cost
mult = undefined

-- | Compute unit cost from cost and length of yarn
slash  :: Cost -> Length-> UnitCost
slash = undefined

-- | Add two costs
add :: Cost -> Cost-> Cost
add a b = a + b

-- | Subtract two costs
sub :: Cost -> Cost-> Cost
sub a b = a - b