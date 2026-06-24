import numpy as np

# =========================
# 1. ARRAY CREATION
# =========================

a = np.array([1,2,3,4,5])

print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.full((2,3),10))

print(np.arange(1,11,2))

print(np.linspace(0,10,5))

print(np.eye(3))

print(np.random.rand(2,3))
print(np.random.randint(1,100,(2,3)))

print(a.dtype)
print(a.shape)
print(a.size)
print(a.ndim)

# =========================
# 2. ARRAY INFORMATION
# =========================

print(a.shape)
print(a.size)
print(a.ndim)
print(a.dtype)

# =========================
# 3. INDEXING
# =========================

print(a[0])
print(a[-1])

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr[1,2])

# =========================
# 4. SLICING
# =========================

print(a[1:4])

print(arr[:,1])

print(arr[0:2,1:3])

# =========================
# 5. RESHAPING
# =========================

b = np.array([1,2,3,4,5,6])

print(b.reshape(2,3))

print(arr.flatten())

print(arr.ravel())

print(arr.T)

# =========================
# 6. MATHEMATICAL OPERATIONS
# =========================

print(a + 10)
print(a - 10)
print(a * 10)
print(a / 10)
print(a ** 2)

c = np.array([10,20,30,40,50])

print(a + c)
print(a - c)
print(a * c)
print(a / c)

# =========================
# 7. AGGREGATE FUNCTIONS
# =========================

print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.min(a))
print(np.max(a))
print(np.std(a))
print(np.var(a))
print(np.prod(a))

print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))

# =========================
# 8. SORTING
# =========================

d = np.array([5,2,8,1,9])

print(np.sort(d))

print(np.argsort(d))

# =========================
# 9. FILTERING
# =========================

print(a[a > 3])

print(a[a % 2 == 0])

# =========================
# 10. CONDITIONAL SELECTION
# =========================

print(np.where(a > 3))

print(np.where(a > 3,"Yes","No"))

# =========================
# 11. COMBINING ARRAYS
# =========================

x = np.array([1,2,3])
y = np.array([4,5,6])

print(np.concatenate((x,y)))

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

print(np.vstack((arr1,arr2)))

print(np.hstack((arr1,arr2)))

# =========================
# 12. SPLITTING ARRAYS
# =========================

z = np.array([1,2,3,4])

print(np.split(z,2))

m = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])

print(np.vsplit(m,2))

print(np.hsplit(m,2))

# =========================
# 13. UNIQUE VALUES
# =========================

u = np.array([1,2,2,3,3,3])

print(np.unique(u))

print(np.unique(u,return_counts=True))

# =========================
# 14. BROADCASTING
# =========================

print(a + 10)

arr3 = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr3 + np.array([1,2,3]))

# =========================
# 15. RANDOM MODULE
# =========================

print(np.random.rand())

print(np.random.randn())

print(np.random.randint(1,100))

np.random.seed(42)

# =========================
# 16. MATRIX CREATION
# =========================

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

# =========================
# 17. MATRIX OPERATIONS
# =========================

print(A + B)

print(A - B)

print(A * B)

print(A @ B)

print(np.dot(A,B))

print(np.matmul(A,B))

# =========================
# 18. LINEAR ALGEBRA
# =========================

print(np.linalg.det(A))

print(np.linalg.inv(A))

print(np.linalg.eig(A))

print(np.linalg.norm(A))

print(np.linalg.matrix_rank(A))

# =========================
# 19. DOT PRODUCT
# =========================

p = np.array([1,2,3])

q = np.array([4,5,6])

print(np.dot(p,q))

# =========================
# 20. MULTIPLE MATRIX MULTIPLICATION
# =========================

C = np.array([
    [1,0],
    [0,1]
])

print(np.linalg.multi_dot([A,B,C]))

# =========================
# 21. STATISTICS
# =========================

print(np.mean(a))

print(np.median(a))

print(np.std(a))

print(np.var(a))

print(np.percentile(a,50))

x = np.array([1,2,3,4,5])

y = np.array([2,4,6,8,10])

print(np.corrcoef(x,y))

print(np.cov(x,y))

# =========================
# 22. MESHGRID
# =========================

x = np.arange(5)

y = np.arange(5)

X, Y = np.meshgrid(x,y)

print(X)

print(Y)

# =========================
# 23. DISTANCE FORMULA
# =========================

point = np.array([3,4])

print(np.linalg.norm(point))

p1 = np.array([1,2])

p2 = np.array([4,6])

print(np.linalg.norm(p1-p2))

# =========================
# 24. USEFUL FUNCTIONS FOR ML
# =========================

a = np.array([1,2,3,4,5])

print(np.isnan(a))

print(np.isinf(a))

print(np.clip(a,0,100))

print(np.round(a,2))

print(np.sqrt(a))

print(np.log(a))

print(np.exp(a))