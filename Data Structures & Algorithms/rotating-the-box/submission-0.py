class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        def apply_gravity(row):
            n = len(row) 
            write_pos = n - 1

            for i in range(n-1, -1, -1):
                if row[i] == "*":
                    for j in range(write_pos, i, -1):
                        row[j] = "."
                    write_pos = i - 1
                elif row[i] != ".":
                    row[write_pos] = row[i]
                    write_pos -= 1

            for i in range(write_pos, -1, -1):
                if row[i] != "*":
                    row[i] = "."

            return row

        for row in boxGrid:
            apply_gravity(row)

        return [list(row) for row in zip(*boxGrid[::-1])]