---
layout: post
title:  "Money Records"
date:   2016-02-12 12:00:00 -0800
categories: projects
summary: "Brief description of how I keep track of my expenditures."
---

About two years ago, I started keeping really good records of all of my finances. Whenever I got money, or spent money, I recorded the transaction in this file, with an amount, a date, a note of how I paid (cash, credit/debit card), and fancy hierarchical tags -- really thorough records. It worked for a couple weeks until I stopped doing it, because taking thirty seconds to figure out the exact right set of tags for a transaction is just *really a pain*.

About three weeks ago, I started keeping okay records of all my finances. Whenever I get money, or spend money, I record the amount, the date, and the general category (e.g. eat-out, groceries, income, rent). I'm having zero trouble keeping this going.

Here's how the whole shebang works:

- Whenever I spend money, I fire up a terminal next time it's convenient, and type

        transaction 3.56 eat-out

  or

        transaction 123.45 income --note 'paycheck'

  or whatever. The amount I spent, the general category (e.g. "eat-out", "groceries", "rent", "income"), the current date (or one I provide), and optionally a note; all those are recorded in a file. [Here's the script](/resources/code/transaction.py).

- When I want to crunch some numbers, I open up [a Mathematica notebook](/resources/code/budget.nb) that loads up the data in that CSV file, and makes pretty plots and pie charts:

  ![categorization of my finances since January 18](/resources/img/transaction-breakdown.png)

It's that easy! It is seriously that easy. And now I will be able to keep excellent track of where my money goes.

I think the moral of the story is for many X, if you know you're likely to put too much work into X and then fail completely as a result, you should purposefully paint yourself into a corner so that you *can't* put too much work into doing X.
