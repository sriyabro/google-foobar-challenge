# google-foobar-challenge
### My experience so far on Google Foobar Challenge
---

### Level 1
#### The Challenge:  Braille Translation
Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating her space station. You figure printing out Braille signs will help them, and – since you’ll be promoting efficiency at the same time – increase your chances of a promotion. Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2×3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda’s command can feel the bumps on the signs and “read” the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:

    1 4
    2 5
    3 6

So given the plain text word “code”, you get the Braille dots:

    11 10 11 10
    00 01 01 01
    00 10 00 00

Write a function where 1 represents a bump and 0 represents no bump. Put together, “code” becomes the output string “100100101010100110100010”.

Write a function solution(plaintext) that takes a string parameter and returns a string of 1’s and 0’s representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

**Solution:** [braille_translation.py](https://github.com/sriyabro/google-foobar-challenge/blob/main/L1-braille_translation.py)


### Level 2
#### Challenge 1: Lovely Lucky Lambs
Being a henchman isn’t all drudgery. Occasionally, when Commander Lambda is feeling generous, she’ll hand out Lucky LAMBs (Lambda’s All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks, a pillow for their bunks, or even a third daily meal!

However, actually passing out LAMBs isn’t easy. Each henchman squad has a strict seniority ranking which must be respected – or else the henchmen will revolt and you’ll all get demoted back to minions again!

There are 4 key rules which you must follow in order to avoid a revolt: 1. The most junior henchman (with the least seniority) gets exactly 1 LAMB. (There will always be at least 1 henchman on a team.) 2. A henchman will revolt if the person who ranks immediately above them gets more than double the number of LAMBs they do. 3. A henchman will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs they get. (Note that the two most junior henchmen won’t have two subordinates, so this rule doesn’t apply to them. The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.) 4. You can always find more henchmen to pay – the Commander has plenty of employees. If there are enough LAMBs left over such that another henchman could be added as the most senior while obeying the other rules, you must always add and pay that henchman.

Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen must get a positive integer number of LAMBs.

Write a function called solution(total_lambs), where total_lambs is the integer number of LAMBs in the handout you are trying to divide. It should return an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy as possible, respectively) while still obeying all of the above rules to avoid a revolt. For instance, if you had 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore, answer(10) should return 4-3 = 1.

To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts: you can expect total_lambs to always be between 10 and 1 billion (10 ^ 9).

**Solution:** [lovely_lucky_lambs.py](https://github.com/sriyabro/google-foobar-challenge/blob/main/L2-1-lovely_lucky_lambs.py)
