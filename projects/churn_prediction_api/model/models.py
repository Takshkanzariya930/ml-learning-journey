from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal


class UserInput(BaseModel):

    Gender: Annotated[
        Literal["Male", "Female"],
        Field(..., description="Customer gender")
    ]

    Senior_Citizen: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Is customer a senior citizen")
    ]

    Partner: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Does customer have a partner")
    ]

    Dependents: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Does customer have dependents")
    ]

    Tenure_Months: Annotated[
        int,
        Field(..., ge=0, description="Customer tenure in months")
    ]

    Phone_Service: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Phone service subscription")
    ]

    Multiple_Lines: Annotated[
        Literal["Yes", "No", "No phone service"],
        Field(..., description="Multiple phone lines")
    ]

    Internet_Service: Annotated[
        Literal["DSL", "Fiber optic", "No"],
        Field(..., description="Internet service type")
    ]

    Online_Security: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Online security service")
    ]

    Online_Backup: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Online backup service")
    ]

    Device_Protection: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Device protection plan")
    ]

    Tech_Support: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Tech support service")
    ]

    Streaming_TV: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Streaming TV service")
    ]

    Streaming_Movies: Annotated[
        Literal["Yes", "No", "No internet service"],
        Field(..., description="Streaming movies service")
    ]

    Contract: Annotated[
        Literal["Month-to-month", "One year", "Two year"],
        Field(..., description="Contract type")
    ]

    Paperless_Billing: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Paperless billing")
    ]

    Payment_Method: Annotated[
        Literal[
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ],
        Field(..., description="Payment method")
    ]

    Monthly_Charges: Annotated[
        float,
        Field(..., ge=0, description="Monthly charges")
    ]

    @computed_field
    @property
    def Total_Charges(self) -> float:
        return round(self.Tenure_Months * self.Monthly_Charges, 2)
    
    
class APIOutput(BaseModel):
    
    Prediction: Annotated[
        str,
        Field(..., description="Prediction of will Customer Churn or Not")
    ]
    
    Confidence: Annotated[
        float,
        Field(..., ge=0, le=1, description="Confidence in prediction made (Between 0.0 and 1.0)")
    ]