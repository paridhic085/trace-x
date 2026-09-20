import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "output" / "alerts.json"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "risk.json"


#Anomalies ko jo points assign hue hai voh-
RISK_WEIGHTS = {
    "RAPID_ONWARD_TRANSFER": 30,
    "HIGH_TRANSACTION_VELOCITY": 20,
    "SHARED_DEVICE": 15,
    "REPEATED_BENEFICIARY": 15
}


def load_alerts():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def calculate_risk(alerts):
    entity_scores = {}
    entity_alerts = {}

    for alert in alerts:
        entity = alert["entity"]
        alert_type = alert["type"]

        points = RISK_WEIGHTS.get(alert_type, 10)

        if entity not in entity_scores:
            entity_scores[entity] = 0
            entity_alerts[entity] = []

        entity_scores[entity] += points
        entity_alerts[entity].append(alert)

    results = []

    for entity, score in entity_scores.items():

        # Keep score between 0 and 100
        score = min(score, 100)

        if score >= 70:
            level = "HIGH"
        elif score >= 40:
            level = "MEDIUM"
        else:
            level = "LOW"

        results.append({
            "entity": entity,
            "risk_score": score,
            "risk_level": level,
            "alert_count": len(entity_alerts[entity]),
            "alert_types": [
                alert["type"]
                for alert in entity_alerts[entity]
            ],
            "evidence": [
                evidence
                for alert in entity_alerts[entity]
                for evidence in alert.get("evidence", [])
            ]
        })

    results.sort(
        key=lambda item: item["risk_score"],
        reverse=True
    )

    return results


def export_risk(risk_results):
    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(risk_results, file, indent=2)

    print(f"Risk report exported to: {OUTPUT_FILE}")


def main():
    alerts = load_alerts()

    risk_results = calculate_risk(alerts)

    print("\nRisk Analysis:")
    print("-" * 60)

    for result in risk_results:
        print(
            f'{result["entity"]} | '
            f'Score: {result["risk_score"]} | '
            f'Level: {result["risk_level"]} | '
            f'Alerts: {result["alert_count"]}'
        )

    export_risk(risk_results)


if __name__ == "__main__":
    main()