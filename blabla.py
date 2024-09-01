def calculate_length(s: str) -> int:
    i = 0
    length = 0

    while i < len(s):
        if s[i] == '(':
            # Reading the marker (N1xN2)
            i += 1
            marker = ''
            while s[i] != ')':
                marker += s[i]
                i += 1
            i += 1  # Skip the closing ')'

            N1, N2 = map(int, marker.split('x'))
            segment = s[i:i+N1]

            # Calculate the length of the segment recursively
            length += N2 * calculate_length(segment)
            i += N1  # Move the index forward by N1
        else:
            # Regular character, just increase the length
            length += 1
            i += 1

    return length

# Testing with the provided string
s = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
print(calculate_length(s))