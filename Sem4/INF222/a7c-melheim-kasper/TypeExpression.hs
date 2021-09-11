module TypeExpression where

--Imports
import State
import Data.Word (Word64, Word32, Word8, Word16)
import Data.Int (Int64, Int16, Int8, Int32)
import Data.Array ()

--Data TypeExpression
data TypeExpression = BInt8 Int8 
    | BInt16 Int16
    | BInt32 Int32 
    | BInt64 Int64
    | BBool Bool 
    | BString String
    | BFloat Float
    | BDouble Double
    | BChar Char
    | BArray [TypeExpression]
    deriving (Show, Read, Eq)

--Data Type
data Type = TInt8 
    | TBool 
    | TChar
    | TFloat
    | TString 
    | TDouble
    | TArray
    | TInt16
    | TInt32
    | TInt64
    deriving (Show, Read, Eq)

--Gets the size of a typeexpression as memorysize
sizeof :: TypeExpression -> MemorySize
sizeof (BBool _) = 1
sizeof (BInt8 _) = 1
sizeof (BInt16 _) = 2
sizeof (BInt32 _) = 4
sizeof (BInt64 _) = 8
sizeof (BDouble _) = 25
sizeof (BFloat _) = 13
sizeof (BChar _) = 1
sizeof (BArray x) = fromIntegral (length x) * 2
sizeof (BString x) = fromIntegral (length x) + 1

--Converts from type expression to word8
write :: TypeExpression -> [Word8]
write (BBool a) = toWords a
write (BInt8 a) = toWords a
write (BInt16 a) = toWords a
write (BInt32 a) = toWords a
write (BInt64 a) = toWords a
write (BDouble a) =  toWords a
write (BChar a) = toWords a
write (BFloat a) = toWords a
write (BString a) = [c | c <- (toWords a), c /= 0 ]

--Gets type from type expression
getType :: TypeExpression -> Type
getType (BBool _) = TBool
getType (BInt8 _) = TInt8
getType (BInt16 _) = TInt16
getType (BInt32 _) = TInt32
getType (BInt64 _) = TInt64
getType (BDouble _) = TDouble
getType (BFloat _) = TFloat
getType (BChar _) = TChar
getType (BString _) = TString