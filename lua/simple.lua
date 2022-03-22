--####################################################
--                      LUA
--####################################################
-- Index in table begin at 1



--=================================================
--               ARITHMETIC
--=================================================

-- Multiplication
a = 5*9 -- a = 45

-- Modulo
b = 11%5 -- b = 1

-- String concatenation
c = "test"
d = "hui"
d = d..c -- d = "huittest"

-- Loop
val_end = 10
step = 1
for i = 0, val_end, step do
    print(i)
end

--=================================================
--               FUNCTIONS
--=================================================

function foo(arg1, arg2, arg3)
    return arg1*arg2*arg3, arg1+arg2+arg3
end

-- return max between 2 number
function max(num1, num2)
   if (num1 > num2) then
      result = num1;
   else
      result = num2;
   end
   return result;
end
print("The maximum of the two numbers is ",max(10,4))

res1, res2 = foo(3,5,6)
print(res1, res2)

-- incoditional block

do
    local var1 = 10
end

print(var1) --return nil


--=================================================
--               TABLE
--=================================================

-- Declaration
a = { 5, "foo", [[C:\Lua\Lua.exe]], 'bar', 42 }
print(a[1], a[2], a[3], a[4], a[5])

-- Insertion
table.insert(a, "lorem")
print(table.concat(a, "   "))

-- Deletion
table.remove(a, 6) -- Remove the 6th element on the list

-- Loop in table
for index, value in pairs(a) do
    print(index, value)
end

-- Remove in loop
for index, value in pairs(a) do
    if value =="foo" then
        table.remove(a, index)
    end
end
print(table.concat(a, "   "))

--=================================================
--               STRING
--=================================================

-- Find
variable = "bonjour"
debut, fin  = string.find(variable, "our") -- return 5 and 7 (index)

-- Format
print(string.format("%s : %s : %i : %i", "TEST", "OK", 7, 187)) -- %s : string, %i : number

--gsub (replace)
print(string.gsub(" bonjour world, bonjour", "bonjour", "hello")) -- return string result and number of replacement

-- Length
print(string.len("ihyuflgffi"))
--=================================================
--               MATH MODULE
--=================================================
-- Pi
print(math.pi)

-- Modulo (similar to '%' operator)
print(math.fmod(11,5))