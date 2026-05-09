class ThreatScorer:

    def calculate_score(self, indicators):

        score = 0

        # Blacklisted malware/process
        if indicators["blacklisted"]:
            score += 60

        # Executed from suspicious locations
        if indicators["suspicious_path"]:
            score += 50

        # Abnormal CPU usage
        if indicators["high_cpu"]:
            score += 30

        # Abnormal memory usage
        if indicators["high_memory"]:
            score += 25

        # Encoded PowerShell commands
        if indicators["encoded_powershell"]:
            score += 50

        # Office spawning shells
        if indicators["office_child_process"]:
            score += 45

        return score