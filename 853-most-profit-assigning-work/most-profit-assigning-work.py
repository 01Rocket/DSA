class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Pair jobs and sort by difficulty
        jobs = list(zip(difficulty, profit))
        jobs.sort()

        # Sort workers by ability
        worker.sort()

        total_profit = 0
        max_profit = 0
        job_index = 0

        # Assign the best possible job to each worker
        for ability in worker:
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1

            total_profit += max_profit

        return total_profit