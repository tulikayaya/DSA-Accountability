<h2><a href="https://leetcode.com/problems/longest-common-prefix">14. Longest Common Prefix</a></h2><h3>Easy</h3><hr><p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>

---

## Approach

The idea is to compare characters **column by column** across all strings.

We use the **first string as a reference** and iterate through its characters. For each character position `i`, we check whether all other strings contain the same character at that position.

Steps:
1. Initialize an empty result string `res`.
2. Iterate through each character index `i` of the first string.
3. For each string in the list:
   - If the current index `i` is equal to the string length, the prefix cannot continue.
   - If the character at index `i` does not match the character in the first string, stop and return the prefix found so far.
4. If all strings match at index `i`, append that character to `res`.
5. Continue until a mismatch occurs or the first string ends.

This approach effectively checks each "column" of characters across all strings.

---

## Solution

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
                
            res += strs[0][i]

        return res