def fun(customer,grumpy,k):
    happy=0
    for i in range(len(customer)):
        if grumpy[i]==0:
            happy+=customer[i]
    l=0
    r=k-1
    window_sum=0
    for i in range(l,r+1):
        if grumpy[i]==1:
            window_sum+=customer[i]
        else:
            window_sum+=0
    max_rescued=window_sum
    while(r<len(customer)-1):
        if grumpy[l] == 1:
            window_sum -= customer[l]
        l += 1
        r += 1
        if grumpy[r] == 1:
                window_sum += customer[r]
        max_rescued = max(max_rescued, window_sum)
    ans=happy+max_rescued
    return ans

customer=[1,0,1,2,1,1,7,5]
grumpy=[0,1,0,1,0,1,0,1]
print(fun(customer,grumpy,3))

# Sliding Window — LeetCode 1052
# Grumpy Bookstore Owner
# 🔹 Problem Idea

# Owner can use a technique for minutes consecutive minutes.

# During those minutes:

# grumpy = 1 → customers become happy

# We need to maximize total happy customers.

# 🔹 Key Observation

# Divide customers into 2 groups:

# 1. Already Happy
# grumpy[i] == 0

# These customers are already happy.

# happy += customers[i]
# 2. Can Be Rescued
# grumpy[i] == 1

# These customers are unhappy.

# If we apply the technique during their minute:

# window_sum += customers[i]
# 🔹 Main Formula
# Answer = Already Happy + Maximum Rescued
# 🔹 Why Sliding Window?

# The technique can be used for exactly:

# minutes

# consecutive minutes.

# Therefore:

# Window size = minutes

# We find the window that contains the maximum number of rescuable customers.

# 🔹 What does window_sum represent?
# window_sum

# = Number of unhappy customers inside the current window.

# Only count:

# grumpy[i] == 1

# Remember:

# grumpy[i]   → tells IF we count
# customers[i] → tells HOW MUCH we count
# 🔹 First Window

# Set:

# l = 0
# r = k - 1
# window_sum = 0

# Calculate the rescue value of the first window.

# for i in range(l, r + 1):
#     if grumpy[i] == 1:
#         window_sum += customers[i]

# Then:

# max_rescued = window_sum
# 🔹 Sliding the Window

# When moving:

# [1, 2, 3] → [2, 3, 4]
# Step 1: Remove outgoing element
# if grumpy[l] == 1:
#     window_sum -= customers[l]
# Step 2: Move pointers
# l += 1
# r += 1

# ⚠️ Always move pointers.

# Step 3: Add incoming element
# if grumpy[r] == 1:
#     window_sum += customers[r]
# Step 4: Update maximum
# max_rescued = max(max_rescued, window_sum)
# 🔥 Sliding Pattern to Remember
# REMOVE
#    ↓
# MOVE
#    ↓
# ADD
#    ↓
# UPDATE MAX

# More specifically:

# if outgoing is grumpy → subtract

# move l and r → ALWAYS

# if incoming is grumpy → add

# update max
# ⚠️ Common Mistake

# ❌ Don't do:

# if grumpy[l] == 1:
#     window_sum -= customers[l]
#     l += 1
#     r += 1

# Because if:

# grumpy[l] == 0

# then l and r won't move.

# ✅ Do:

# if grumpy[l] == 1:
#     window_sum -= customers[l]

# l += 1
# r += 1
# 🧠 Most Important Things
# 1. Count already happy customers separately.

# 2. Window size = minutes.

# 3. window_sum = rescuable unhappy customers.

# 4. grumpy[i] == 1 → count customers[i].

# 5. grumpy[i] == 0 → don't count in window_sum.

# 6. Sliding:
#    remove → move → add → max

# 7. Final:
#    answer = happy + max_rescued
# ⏱ Complexity
# Time  : O(n)
# Space : O(1)
# 🧠 One-line memory trick

# Already happy + best window of unhappy customers = maximum happy customers.