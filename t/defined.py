print("1..5")

import perl
perl.eval("""

sub foo;

sub bar { }

@baz = ();

$Foo::bar = 33;

""")

if perl.defined("baz") or perl.defined("baz"): print("not ", end=' ')
print("ok 1")

if not perl.defined("foo") and perl.defined("bar"): print("not ", end=' ')
print("ok 2")

if not perl.defined("@baz"): print("not ", end=' ')
print("ok 3")

if not perl.defined("$Foo::bar"): print("not ", end=' ')
print("ok 4")

try:
    if perl.defined(" $Foo::bar"): print("not ", end=' ')
except perl.PerlError:
    print("ok 5")

