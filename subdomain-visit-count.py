class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        
        for cp in cpdomains:
            count_str, domain = cp.split()
            count = int(count_str)
            
            parts = domain.split(".")
            
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                counts[subdomain] = counts.get(subdomain, 0) + count
        
        result = []
        for domain, count in counts.items():
            result.append(str(count) + " " + domain)
        
        return result

        
