# 811. Subdomain Visit Count

from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        for phrase in cpdomains:
            count, dom = phrase.split()
            count = int(count)
            subs = dom.split(".")
            for i in range(len(subs)-1, -1, -1):
                cp = ".".join(subs[i:])
                domains[cp] += count
        out = []
        for k, v in domains.items():
            out.append(str(v) + " " + k)

        return out
