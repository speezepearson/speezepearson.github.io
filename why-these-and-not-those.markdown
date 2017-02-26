---
layout: post
title:  "Why these and not those?"
date:   2017-01-13 12:00:00 -0800
hidden: true
---

Let me share my favorite game with you.

> I have a rule. I'll answer questions of the form, "Does _this_ satisfy the rule?"
>
> Identify the rule.

I call this game, "Why these and not those?" I've seen it by a few different names:

* In **[the 2-4-6 game](https://en.wikipedia.org/wiki/Bongard_problem)**, the rule applies to triplets of numbers.
    (The name of the game comes from the fact that "2-4-6 satisfies the rule" is a freebie when using the canonical rule that
    <span style="border: 1px solid gray">
      <a onclick="
        if (this.innerHTML=='show') {
          this.innerHTML='hide';
          $('#246-rule').css('color','rgba(0,0,0,1)')
        } else {
          this.innerHTML='show';
          $('#246-rule').css('color','rgba(0,0,0,0)')
        }">show</a>
      <span id="246-rule" style="color: rgba(0,0,0,0)">the triplet of numbers must be sorted from smallest to largest</span>
    </span>.

* In **20 questions**, the rule applies to properties an object might have. (You're also guaranteed that there exists some object that has all of the "yes" properties and none of the "no" properties.)

* In "Green Glass Door," the rule applies to objects. There is a door that allows some objects to pass through, but rejects others.
    (As with 2-4-6, there's a canonical rule:
    <span style="border: 1px solid gray">
      <a onclick="
        if (this.innerHTML=='show') {
          this.innerHTML='hide';
          $('#ggd-rule').css('color','rgba(0,0,0,1)')
        } else {
          this.innerHTML='show';
          $('#ggd-rule').css('color','rgba(0,0,0,0)')
        }">show</a>
      <span id="ggd-rule" style="color: rgba(0,0,0,0)">the object must be spelled with a double letter (e.g. "green," "glass," "door")</span>
    </span>)

* In **[Bongard problems](https://en.wikipedia.org/wiki/Bongard_problem)**, there are two sets of shapes: the ones on the left obey the rule, and the ones on the right violate it. (This is a non-interactive version of the game, more a puzzle.) For example,

    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Bongard_problem_convex_polygons.svg" style="max-width:30em" />

<br/>

The game is very simple and very easy to customize. Some variations:

* My rule applies to doodles. Doodle things and I'll tell you which ones satisfy the rule.
* My rule applies to words. Say words and I'll tell you which ones satisfy the rule.
* My rule applies to numbers. Cities. Chemicals. People. Web sites. Plants. Machines. Insects. Books. Board games. Diseases. Professions. Monarchs. Memes. Clothing items. Mixed drinks. Cognitive biases. Funny faces. Species of snake. Kinds of furniture. Permutations of the letters of the alphabet. Directed acyclic graphs. Disney princesses. Celestial bodies. Musical instruments. Chores. Fabrics. Kinks. Brands. Phyla. Things in the same room as you. Activities you do with people. Unusual uses for objects. Categories of thing. Rules you could use for this game. Really, any class of objects where examples are easy to specify and reason about.

<br/>

I love this game because (a) it requires no equipment, (b) it has excellent replay value, and (c) it is a pure, unadulterated exercise for your most important skill: pattern recognition. On a math-nerd note, it's also pleasingly simple from an information-theoretic perspective: every (good) question gives you one bit of information, so the number of questions you have to ask is just the entropy of your probability distribution over potential rules.

One last thought: you can generalize this game *still further* by allowing the response to be *anything,* not just "yes" or "no." (I grew up thinking that "Make me say six" was a common game for parents to play with their children: the parent thinks of some mathematical function, like $(x-4)^2 - 3$, and the child names numbers, and the parent responds with the function applied to those numbers; the child is supposed identify the function and figure out how to make the parent say six. I learned a few years ago that no, that wasn't normal, that was just my dad.)
