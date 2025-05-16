class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # M1: bruteforce (O(n.m) time, O(1) space)
        # count = 0 
        # while students:
        #     if students[0] == sandwiches[0]:
        #         students.pop(0)
        #         sandwiches.pop(0)
        #         count = 0
        #     else:
        #         last = students.pop(0)
        #         students.append(last)
        #         count += 1
        #     if count == len(students):
        #         break
        # return len(students)


        # M2:  O(n) time, O(1) space
        # count the number of students want round and square sandwich respectively
        # for each sandwich in the sandwiches stack: (the current sandwich in each iteration is the one on top)
        #   if there's still student who want that sandwich, decrement the count of the associated student counter
        #   else: no one want the current sandwich -> return the number of student left
        countStudents = [0,0] # countStudents[0] is count of round student, countStudents[1] is count of square student
        for s in students:
            countStudents[s] += 1
        for sandwich in sandwiches:
            if countStudents[sandwich] != 0:
                countStudents[sandwich] -= 1
            else: # no one else wants that sandwich type
                break
        return countStudents[0] + countStudents[1] 
