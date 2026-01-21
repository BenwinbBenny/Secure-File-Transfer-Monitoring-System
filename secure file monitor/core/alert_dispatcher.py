from core.audit_logger import record_event

class AlertDispatcher:
    @staticmethod
    def dispatch(severity, summary, metadata):
        print(f"\n[DLP ALERT | {severity}] {summary}")
        record_event(
            "SECURITY_ALERT",
            {
                "severity": severity,
                "summary": summary,
                "metadata": metadata
            },
            severit
        )

