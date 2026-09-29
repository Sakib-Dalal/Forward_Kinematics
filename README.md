## 1. SCARA Forward Kinematics

The three active values in our code are:

```math
q_1 = \text{base\_arm\_motor}
```

```math
q_2 = \text{arm\_motor}
```

```math
q_3 = \text{shaft\_linear\_motor}
```

The coursework calls the shaft displacement $q_4$, but in our function it is the third input, so we name it $q_3$.

## Given vectors

### Base → Joint 1

$$
\mathbf{P}_{\text{base}} =
\begin{bmatrix}
0.060 \\
0 \\
0.220
\end{bmatrix}
$$

### Joint 1 → Joint 2

$$
\mathbf{L}_1 =
\begin{bmatrix}
0.310 \\
0.005 \\
-0.004
\end{bmatrix}
$$

### Joint 2 → TCP

$$
\mathbf{L}_2 =
\begin{bmatrix}
0.2545 \\
-0.005 \\
q_3 - 0.034
\end{bmatrix}
$$

These values come from the SCARA robot specification in Coursework_1_2627.

---

## Rotation formula

A rotation around the $Z$-axis is:

$$
R_z(\theta) =
\begin{bmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

The first link rotates by $q_1$.

The second link rotates by $q_1 + q_2$.

---

## Complete SCARA formula

$$
\boxed{
\mathbf{P}_{\text{TCP}} =
\mathbf{P}_{\text{base}}
+ R_z(q_1)\mathbf{L}_1
+ R_z(q_1 + q_2)\mathbf{L}_2
}
$$

### X coordinate

$$
\boxed{
\begin{aligned}
x ={}& 0.060
+ 0.310\cos(q_1)
- 0.005\sin(q_1) \\
&+ 0.2545\cos(q_1 + q_2)
+ 0.005\sin(q_1 + q_2)
\end{aligned}
}
$$

The last term is positive because:

$$
-(-0.005)\sin(q_1 + q_2)
= +0.005\sin(q_1 + q_2)
$$

### Y coordinate

$$
\boxed{
\begin{aligned}
y ={}& 0.310\sin(q_1)
+ 0.005\cos(q_1) \\
&+ 0.2545\sin(q_1 + q_2)
- 0.005\cos(q_1 + q_2)
\end{aligned}
}
$$

### Z coordinate

$$
z = 0.220 - 0.004 + (q_3 - 0.034)
$$

Therefore:

$$
\boxed{z = 0.182 + q_3}
$$

It is still useful to keep the full version in the code because it shows where every offset came from:

$$
0.220 - 0.004 + q_3 - 0.034
$$

---

## 2. Niryo Ned Forward Kinematics

For Ned:

$$
q_1 = \text{joint\_1}, \qquad
q_2 = \text{joint\_2}, \qquad
q_3 = \text{joint\_3}
$$

The coursework gives:

$$
h = 0.1715, \qquad
A = 0.2210, \qquad
B = 0.0120, \qquad
U = 0.03185, \qquad
V = 0.23000
$$

---

## Step 1 — Shoulder → Elbow

The horizontal component is:

$$
\boxed{r_1 = A\cos(q_2) - B\sin(q_2)}
$$

Using the actual values:

$$
\boxed{r_1 = 0.2210\cos(q_2) - 0.0120\sin(q_2)}
$$

The vertical component is:

$$
\boxed{z_1 = A\sin(q_2) + B\cos(q_2)}
$$

or:

$$
\boxed{z_1 = 0.2210\sin(q_2) + 0.0120\cos(q_2)}
$$

---

## Step 2 — Elbow → TCP

The second section depends on $q_2 + q_3$.

The horizontal component is:

$$
\boxed{r_2 = U\cos(q_2 + q_3) - V\sin(q_2 + q_3)}
$$

Using the dimensions:

$$
\boxed{r_2 = 0.03185\cos(q_2 + q_3) - 0.23000\sin(q_2 + q_3)}
$$

The vertical component is:

$$
\boxed{z_2 = U\sin(q_2 + q_3) + V\cos(q_2 + q_3)}
$$

or:

$$
\boxed{z_2 = 0.03185\sin(q_2 + q_3) + 0.23000\cos(q_2 + q_3)}
$$

---

## Step 3 — Total horizontal distance

Add the two horizontal components:

$$
\boxed{r = r_1 + r_2}
$$

Therefore:

$$
\boxed{
\begin{aligned}
r ={}& A\cos(q_2) - B\sin(q_2) \\
&+ U\cos(q_2 + q_3) - V\sin(q_2 + q_3)
\end{aligned}
}
$$

Substituting the actual numbers:

$$
\boxed{
\begin{aligned}
r ={}& 0.2210\cos(q_2) - 0.0120\sin(q_2) \\
&+ 0.03185\cos(q_2 + q_3)
- 0.23000\sin(q_2 + q_3)
\end{aligned}
}
$$

---

## Step 4 — Total $Z$ coordinate

The shoulder is already at height $h = 0.1715$.

Therefore:

$$
\boxed{z = h + z_1 + z_2}
$$

Expanded:

$$
\boxed{
\begin{aligned}
z ={}& h
+ A\sin(q_2) + B\cos(q_2) \\
&+ U\sin(q_2 + q_3)
+ V\cos(q_2 + q_3)
\end{aligned}
}
$$

Using the numbers:

$$
\boxed{
\begin{aligned}
z ={}& 0.1715
+ 0.2210\sin(q_2)
+ 0.0120\cos(q_2) \\
&+ 0.03185\sin(q_2 + q_3)
+ 0.23000\cos(q_2 + q_3)
\end{aligned}
}
$$

---

## Step 5 — Apply base rotation $q_1$

We now have the horizontal distance $r$, but we need to convert it into the global coordinates $x$ and $y$.

The coursework specifically states that, unlike the usual convention, Ned's $q_1 = 0$ points along the positive $Y$-axis.

The equations used in our code are:

$$
\boxed{x = -r\sin(q_1)}
$$

$$
\boxed{y = r\cos(q_1)}
$$

### Sanity check

If $q_1 = 0$, then:

$$
x = -r\sin(0) = 0
$$

and:

$$
y = r\cos(0) = r
$$

so the arm points along the positive $Y$-axis, as required by the coursework.

---

## Complete Ned equations

### Horizontal distance

$$
\boxed{
\begin{aligned}
r ={}& 0.2210\cos(q_2) - 0.0120\sin(q_2) \\
&+ 0.03185\cos(q_2 + q_3)
- 0.23000\sin(q_2 + q_3)
\end{aligned}
}
$$

### X coordinate

$$
\boxed{x = -r\sin(q_1)}
$$

### Y coordinate

$$
\boxed{y = r\cos(q_1)}
$$

### Z coordinate

$$
\boxed{
\begin{aligned}
z ={}& 0.1715
+ 0.2210\sin(q_2)
+ 0.0120\cos(q_2) \\
&+ 0.03185\sin(q_2 + q_3)
+ 0.23000\cos(q_2 + q_3)
\end{aligned}
}
$$

---

## Quick summary

| Robot | Formula idea |
| --- | --- |
| **SCARA** | Base offset + rotated Link 1 + rotated Link 2 |
| **Ned** | Calculate arm reach $r$ and height $z$, then rotate $r$ around the base using $q_1$ |

For SCARA:

$$
\boxed{
\mathbf{P}_{\text{TCP}} =
\mathbf{P}_{\text{base}}
+ R_z(q_1)\mathbf{L}_1
+ R_z(q_1 + q_2)\mathbf{L}_2
}
$$

For Ned:

$$
\boxed{r = r_1 + r_2}
$$

$$
\boxed{x = -r\sin(q_1)}
$$

$$
\boxed{y = r\cos(q_1)}
$$

$$
\boxed{z = h + z_1 + z_2}
$$

One important distinction: the **SCARA FK form is essentially supplied by the coursework**, while for **Ned the coursework gives the geometry and asks you to derive the forward kinematics**. Verify the Ned sign conventions against Webots in Task 1C.
