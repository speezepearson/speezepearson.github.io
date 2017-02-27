---
layout: post
title:  "Why these and not those?"
date:   2017-01-13 12:00:00 -0800
hidden: true
examples:
  - name: permutations
    rule: >
      It must take an even number of swaps between two digits to transform the input into 0123456789.
    positive_example: 0123456789
    predicate: >
      function(s) {
        var chars = s.split('');
        var sorted = chars.slice().sort();
        if (!arraysEqual(sorted, '0123456789'.split(''))) throw 'not a permutation';
        return (countInversions(chars)%2 == 0);
      }
    category: "permutations of the digits 0123456789"
    validation: "Input must be a rearrangement of the digits 0-9."
  - name: 246
    rule: >
      The triplet must be sorted, from smallest to largest.
    positive_example: "2, 4, 6"
    predicate: >
      function(s) {
        var words = s.split(',');
        if (words.length !== 3) throw 'not 3 numbers';
        var nums = [parseFloat(words[0]), parseFloat(words[1]), parseFloat(words[2])];
        return arraysEqual(nums, nums.slice().sort(function(a,b){return a - b}));
      }
    category: "triplets of numbers"
    validation: "Input must be a triplet of numbers, separated by commas."
---

Let me share my favorite game with you.

> I have a rule. I'll answer questions of the form, "Does _this_ satisfy the rule?"
>
> Identify the rule.

I call this game, "Why these and not those?" I've seen special cases called by a few different names:

* In **[the 2-4-6 game](https://en.wikipedia.org/wiki/Bongard_problem)**, the rule applies to triplets of numbers.
    (The name of the game comes from the fact that "2-4-6 satisfies the rule" is a freebie when using the canonical rule. You can play, or see the rule, [below](#game-246).)

* In **20 questions**, the rule applies to properties an object might have. (You're also guaranteed that there exists some object that has all of the "yes" properties and none of the "no" properties.)

* In **"Green Glass Door,"** the rule applies to objects. There is a door that allows some objects to pass through, but rejects others.
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

* In **[Zendo](https://en.wikipedia.org/wiki/Zendo_(game))**, the rule applies to arrangements of colored pyramids.

* In **"tree or Stalin,"** somebody has an object in mind, and answers questions of the form "Is it more like \_\_\_\_ or more like \_\_\_\_?" (The traditional first question is, "Is it more like a tree or more like Stalin?") This is trivial to recast into the same shape as 20 questions or Zendo or 2-4-6.

<br/>

The game is very simple and very easy to customize. Some variations:

* My rule applies to doodles. Doodle things and I'll tell you which ones satisfy the rule.
* My rule applies to words. Say words and I'll tell you which ones satisfy the rule.
* My rule applies to numbers. Cities. Chemicals. People. Web sites. Plants. Machines. Insects. Books. Board games. Diseases. Professions. Monarchs. Memes. Clothing items. Mixed drinks. Cognitive biases. Species of snake. Kinds of furniture. Permutations of the letters of the alphabet. Directed acyclic graphs. Disney princesses. Celestial bodies. Musical instruments. Chores. Fabrics. Kinks. Brands. Phyla. Things in the same room as you. Activities you do with people. Unusual uses for objects. Categories of thing. Rules you could use for this game. Really, any class of objects where examples are easy to specify and reason about.


I love this game because (a) it requires no equipment, (b) it has excellent replay value, and (c) it is a pure, unadulterated exercise for your most important skill: pattern recognition. (On a math-nerd note, it's also pleasingly simple from an information-theoretic perspective: every (good) question gives you one bit of information, so the number of questions you have to ask is just the entropy of your probability distribution over potential rules.)

In fact, you can generalize this game still further by allowing the response to be anything, not just "yes" or "no." The goal is still to guess the rule, but the rule-space is much richer. I grew up thinking that "Make me say six" was a common game for parents to play with their children: the parent thinks of some mathematical function, like $(x-4)^2-3$, the child names numbers, and the parent responds with the function applied to those numbers; the child is supposed to identify the function and figure out how to make the parent say "six." I only recently learned that actually, nobody outside my family has ever heard of this game.


Examples
--------

To play this game with someone, you need to choose a category and a rule. A good category makes it easy for them to name examples; a good rule bisects the category into two approximately-equally-sized pieces, with very little subjectivity or gray area. ("Is the book written by a woman?" is a fine rule; "Is the book a classic?" is not.)

Because you need a lot of domain knowledge about the category in order to administer the game, it's hard to play with a computer. But here are a couple of well-defined samples:

<script>
function countInversions(array){
  // Note: this uses a variant of merge sort
  //input handlers
  if (array === undefined) throw new Error("Array must be defined to count inversions");
  if (array.length === 0 || array.length === 1) return 0;
  var tally = 0; // count for inversions
  sort(array); // merge sort the array and increment tally when there are crossovers
  return tally;
  function sort(arr) {
    if (arr.length === 1) return arr;
    var right = arr.splice(Math.floor(arr.length/2), arr.length - 1);
    return merge(sort(arr), sort(right));
  }
  function merge(left, right){
    var merged = [];
    var l = 0, r = 0;
    var multiplier = 0;
    while (l < left.length || r < right.length){
      if (l === left.length){
        merged.push(right[r]);
        r++;
      } else if (r === right.length){
        merged.push(left[l]);
        l++;
        tally += multiplier;
      } else if (left[l] < right[r]) {
        merged.push(left[l]);
        tally += multiplier;
        l++;
      } else {
        merged.push(right[r]);
        r++;
        multiplier++;
      }
    }
    return merged;
  }
}
function arraysEqual(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (a.length != b.length) return false;

  // If you don't care about the order of the elements inside
  // the array, you should sort both arrays here.

  for (var i = 0; i < a.length; ++i) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}
function runGuess($game, test) {
  $game.find('.validation').hide();
  var $input = $game.find('.input');
  var input = $input.val(); $input.val('');
  $input.focus();
  try {
    console.log('hi');
    var $examples = $game.find(test(input) ? '.positive-examples' : '.negative-examples');
    $examples.append($('<li>'+input+'</li>'));
  } catch (e) {
    $game.find('.validation').show();
  }
}
</script>

{% for example in page.examples %}
<div class="game" id="game-{{example.name}}" style="border: 1px solid gray; padding: 1em">
<p>I have a rule that applies to {{example.category}}.</p>

<input class="input" onkeydown="if (event.keyCode==13) { runGuess($('#game-{{example.name}}'), {{example.predicate}});}"/>
<button onclick="runGuess($('#game-{{example.name}}'), {{example.predicate}});">Test</button>
<span class="validation" style="color:red; display:none">{{example.validation}}</span><br/>

Solution: <span style="border: 1px solid gray">
  <a onclick="
    if (this.innerHTML=='show') {
      this.innerHTML='hide';
      $('#{{example.name}}-rule').css('color','rgba(0,0,0,1)')
    } else {
      this.innerHTML='show';
      $('#{{example.name}}-rule').css('color','rgba(0,0,0,0)')
    }">show</a>
  <span id="{{example.name}}-rule" style="color: rgba(0,0,0,0)">{{example.rule}}</span></span>
<table style="width:100%">
  <tr><th>Yes</th><th>No</th></tr>
  <tr>
    <td style="width: 50%; border-right: 1px solid black"><ul class="positive-examples"><li>{{example.positive_example}}</li></ul></td>
    <td style="width: 50%"><ul class="negative-examples"></ul></td>
  </tr>
</table>
</div><br />
{% endfor %}
