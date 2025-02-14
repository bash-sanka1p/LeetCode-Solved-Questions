class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for s in sandwiches:
            print(s, students)
            for i in range(len(students)):
                if students[i]==s:
                    students.pop(i)
                    break
            else:
                break
        return len(students)
        