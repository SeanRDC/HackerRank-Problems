# Compares the returned date with the due date year first, then month, then day. The
# fine is 10000 for a late year, 500 per late month, or 15 per late day.

d1, m1, y1 = map(int, input().split())
d2, m2, y2 = map(int, input().split())

def check_days(d1, d2):
    if d1 > d2:
        return (15 * (d1 - d2))
    else:
        return 0

def same_month(m1, m2):
    if m1 > m2:
        return(500 * (m1 - m2))
    else:
        return 0 

def same_year(d1, d2, m1, m2):
    if m1 == m2:
        return check_days(d1, d2)
    elif m1 > m2:
        return same_month(m1, m2)
    else:
        return 0

def fine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 < y2:
        return 0
    else:
        return same_year(d1, d2, m1, m2)

print(fine(d1, m1, y1, d2, m2, y2))