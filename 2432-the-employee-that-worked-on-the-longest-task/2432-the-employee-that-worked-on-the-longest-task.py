class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev_time,max_t=0,0
        ans=None 
        
        
        for emp_id, time in logs:
            if time-prev_time>max_t:
                max_t=time-prev_time
                
                ans=emp_id
            elif time-prev_time==max_t:
                ans=min(ans,emp_id)
                
            prev_time=time
            
        return ans