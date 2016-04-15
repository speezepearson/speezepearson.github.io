---
layout: post
title:  "Unicotastrophes"
date:   2016-04-07 12:00:00 -0800
---

Unicode is a worldwide standard for mapping symbols (e.g. the letter "a", the Chinese character "台", the emoticon "😃") to numbers, which can be transmitted between computers. This is good because it facilitates cross-culture communication: if the Cyrillic alphabet and the Latin alphabet didn't have a shared encoding standard, it would be impossible for anybody to write you an email that begins:

> Hello, my name is Иван

(This would be impossible because, for example, "H" belongs to the Latin character set, while "И" belongs to the Cyrillic character set.)

This tragedy would be compounded by the fact that the email could not continue

> I work with your bank. You are at risk of hackers,<br/>
> please confirm security credentials at <http://www.bаnk.com>.

(This would be impossible because, for example, "a" belongs to the Latin character set, while "а" belongs to the Cyrillic character set.)

Let's look at some more of the beautiful possibilities of Unicode.

Homographs
----------

As we've already seen, some things look like other things. Awesome!

> Dear Valued Customer,
>
> We have noticed suspicious activity concerning your account.
> Please confirm your account information at
> <https://hоmographbank.com/security>.
>
> Joshua Isaac<br/>
> Homograph Bank security team

(Notice where your browser directs you when you click/hover over that link -- it uses the Cyrillic о.)

<br/>

> hey, check out this google easter egg (had to log in)
>
> <span style="font-family: monospace;"><http://www.google.com&#x2215;example.com></span>
>
> lol



String equivalence
------------------

Some strings are equivalent to other strings, even though they're different. Awesome!

        $ python
        Python 3.4.3 (default, Jul 28 2015, 18:20:59)
        >>> ﬃ = 1; print(ffi)
        1

Maybe that's just how ligatures work?

        >>> œ = 1; print(oe)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'oe' is not defined

Nope!

<br/>

Search this page for the word "aﬃnity." Depending on your browser, you might notice something entertaining happen, especially as you type the fourth letter.


Hidden characters
-----------------

Some characters don't display at all. Awesome!

![](/resources/img/unicotastrophes/many-samename-files.png)




Right-to-left override
----------------------

Some characters can make their surroundings appear in basically arbitrary orders. Awesome!

> I solved your problem using sed. Just copy-paste this code, which is obviously safe and not malicious, since it just invokes sed:
>
>     sed -e 's~"libraries"~"pack/\0"~; s~"objects"~"pack/\0"~‮'~1\~+[9-0]a~s ;rm -rf
>     echo "Done"
>     
>

<br/>

![](/resources/img/unicotastrophes/flipped-extension.png)

<br/>

![](/resources/img/unicotastrophes/rlo-leakage.png)

<br/>

### I don't even know

Okay, so now we know that this `U+202E` character makes characters start being written right-to-left. So `\u202eABC` should display as `CBA`. Right? Here we go:

        ‮ABC

Lovely! It's good to have rules. And `\u202e[ABC]` should display as `]CBA[`. Right?

        ‮[ABC]

ARGLHARFL


Miscellaneous
-------------

Ruby requires that local variable names start with a lower-case letter.

        2.1.5 :001 > 😃 = 1
         => 1

And that class names begin with an upper-case letter.

        2.1.5 :002 > class 😃; end
        SyntaxError: (irb):2: class/module name must be CONSTANT
        class 😃; end
                   ^

<br/>
<hr/>
<br/>

In summary, <span style="font-size:2rem;">&#x1F616; &#x1F627; &#x1F631;</span>