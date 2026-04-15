s = "abbaabcda"

seen = {}
left = 0
ans = 0

for right in range(len(s)):
    if s[right] in seen:
        left = max(left, seen[s[right]] + 1)
    seen[s[right]] = right
    ans = max(ans, right - left + 1)

    print(
        f"right={right}, char={s[right]}, left={left}, "
        f"seen={seen}, ans={ans}"
    )

print(ans)