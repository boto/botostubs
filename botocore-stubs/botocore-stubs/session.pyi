from typing import Optional, overload

from typing_extensions import Literal

import botocore
import botocore.client


class Session(object):
    @overload
    def create_client(
        self,
        service_name: Literal["acm"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ACM": ...

    @overload
    def create_client(
        self,
        service_name: Literal["acm-pca"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ACMPCA": ...

    @overload
    def create_client(
        self,
        service_name: Literal["alexaforbusiness"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.AlexaForBusiness": ...

    @overload
    def create_client(
        self,
        service_name: Literal["amplify"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Amplify": ...

    @overload
    def create_client(
        self,
        service_name: Literal["apigatewaymanagementapi"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ApiGatewayManagementApi": ...

    @overload
    def create_client(
        self,
        service_name: Literal["apigatewayv2"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ApiGatewayV2": ...

    @overload
    def create_client(
        self,
        service_name: Literal["application-autoscaling"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ApplicationAutoScaling": ...

    @overload
    def create_client(
        self,
        service_name: Literal["appmesh"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.AppMesh": ...

    @overload
    def create_client(
        self,
        service_name: Literal["appstream"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.AppStream": ...

    @overload
    def create_client(
        self,
        service_name: Literal["appsync"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.AppSync": ...

    @overload
    def create_client(
        self,
        service_name: Literal["athena"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Athena": ...

    @overload
    def create_client(
        self,
        service_name: Literal["autoscaling"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.AutoScaling": ...

    @overload
    def create_client(
        self,
        service_name: Literal["autoscaling-plans"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.AutoScalingPlans": ...

    @overload
    def create_client(
        self,
        service_name: Literal["backup"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Backup": ...

    @overload
    def create_client(
        self,
        service_name: Literal["batch"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Batch": ...

    @overload
    def create_client(
        self,
        service_name: Literal["budgets"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Budgets": ...

    @overload
    def create_client(
        self,
        service_name: Literal["ce"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CostExplorer": ...

    @overload
    def create_client(
        self,
        service_name: Literal["chime"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Chime": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cloud9"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Cloud9": ...

    @overload
    def create_client(
        self,
        service_name: Literal["clouddirectory"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudDirectory": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cloudformation"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudFormation": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cloudfront"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudFront": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cloudhsm"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudHSM": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cloudhsmv2"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudHSMV2": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cloudsearch"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudSearch": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cloudtrail"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudTrail": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cloudwatch"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudWatch": ...

    @overload
    def create_client(
        self,
        service_name: Literal["codebuild"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CodeBuild": ...

    @overload
    def create_client(
        self,
        service_name: Literal["codecommit"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CodeCommit": ...

    @overload
    def create_client(
        self,
        service_name: Literal["codedeploy"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CodeDeploy": ...

    @overload
    def create_client(
        self,
        service_name: Literal["codepipeline"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CodePipeline": ...

    @overload
    def create_client(
        self,
        service_name: Literal["codestar"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CodeStar": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cognito-identity"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CognitoIdentity": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cognito-idp"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CognitoIdentityProvider": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cognito-sync"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CognitoSync": ...

    @overload
    def create_client(
        self,
        service_name: Literal["comprehend"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Comprehend": ...

    @overload
    def create_client(
        self,
        service_name: Literal["comprehendmedical"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ComprehendMedical": ...

    @overload
    def create_client(
        self,
        service_name: Literal["config"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ConfigService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["connect"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Connect": ...

    @overload
    def create_client(
        self,
        service_name: Literal["cur"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CostandUsageReportService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["datapipeline"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DataPipeline": ...

    @overload
    def create_client(
        self,
        service_name: Literal["datasync"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DataSync": ...

    @overload
    def create_client(
        self,
        service_name: Literal["dax"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DAX": ...

    @overload
    def create_client(
        self,
        service_name: Literal["devicefarm"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DeviceFarm": ...

    @overload
    def create_client(
        self,
        service_name: Literal["directconnect"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DirectConnect": ...

    @overload
    def create_client(
        self,
        service_name: Literal["discovery"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ApplicationDiscoveryService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["dlm"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DLM": ...

    @overload
    def create_client(
        self,
        service_name: Literal["dms"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DatabaseMigrationService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["docdb"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DocDB": ...

    @overload
    def create_client(
        self,
        service_name: Literal["ds"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DirectoryService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["dynamodb"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DynamoDB": ...

    @overload
    def create_client(
        self,
        service_name: Literal["dynamodbstreams"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.DynamoDBStreams": ...

    @overload
    def create_client(
        self,
        service_name: Literal["ec2"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.EC2": ...

    @overload
    def create_client(
        self,
        service_name: Literal["ecr"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ECR": ...

    @overload
    def create_client(
        self,
        service_name: Literal["ecs"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ECS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["efs"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.EFS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["eks"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.EKS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["elasticache"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ElastiCache": ...

    @overload
    def create_client(
        self,
        service_name: Literal["elasticbeanstalk"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ElasticBeanstalk": ...

    @overload
    def create_client(
        self,
        service_name: Literal["elastictranscoder"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ElasticTranscoder": ...

    @overload
    def create_client(
        self,
        service_name: Literal["elb"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ElasticLoadBalancing": ...

    @overload
    def create_client(
        self,
        service_name: Literal["elbv2"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ElasticLoadBalancingv2": ...

    @overload
    def create_client(
        self,
        service_name: Literal["emr"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.EMR": ...

    @overload
    def create_client(
        self,
        service_name: Literal["es"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ElasticsearchService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["events"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.CloudWatchEvents": ...

    @overload
    def create_client(
        self,
        service_name: Literal["firehose"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Firehose": ...

    @overload
    def create_client(
        self,
        service_name: Literal["fms"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.FMS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["fsx"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.FSx": ...

    @overload
    def create_client(
        self,
        service_name: Literal["gamelift"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.GameLift": ...

    @overload
    def create_client(
        self,
        service_name: Literal["glacier"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Glacier": ...

    @overload
    def create_client(
        self,
        service_name: Literal["globalaccelerator"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.GlobalAccelerator": ...

    @overload
    def create_client(
        self,
        service_name: Literal["glue"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Glue": ...

    @overload
    def create_client(
        self,
        service_name: Literal["greengrass"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Greengrass": ...

    @overload
    def create_client(
        self,
        service_name: Literal["guardduty"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.GuardDuty": ...

    @overload
    def create_client(
        self,
        service_name: Literal["iam"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.IAM": ...

    @overload
    def create_client(
        self,
        service_name: Literal["importexport"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ImportExport": ...

    @overload
    def create_client(
        self,
        service_name: Literal["inspector"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Inspector": ...

    @overload
    def create_client(
        self,
        service_name: Literal["iot"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.IoT": ...

    @overload
    def create_client(
        self,
        service_name: Literal["iot-data"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.IoTDataPlane": ...

    @overload
    def create_client(
        self,
        service_name: Literal["iot-jobs-data"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.IoTJobsDataPlane": ...

    @overload
    def create_client(
        self,
        service_name: Literal["iot1click-devices"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.IoT1ClickDevicesService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["iot1click-projects"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.IoT1ClickProjects": ...

    @overload
    def create_client(
        self,
        service_name: Literal["iotanalytics"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.IoTAnalytics": ...

    @overload
    def create_client(
        self,
        service_name: Literal["kafka"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Kafka": ...

    @overload
    def create_client(
        self,
        service_name: Literal["kinesis"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Kinesis": ...

    @overload
    def create_client(
        self,
        service_name: Literal["kinesis-video-archived-media"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.KinesisVideoArchivedMedia": ...

    @overload
    def create_client(
        self,
        service_name: Literal["kinesis-video-media"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.KinesisVideoMedia": ...

    @overload
    def create_client(
        self,
        service_name: Literal["kinesisanalytics"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.KinesisAnalytics": ...

    @overload
    def create_client(
        self,
        service_name: Literal["kinesisanalyticsv2"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.KinesisAnalyticsV2": ...

    @overload
    def create_client(
        self,
        service_name: Literal["kinesisvideo"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.KinesisVideo": ...

    @overload
    def create_client(
        self,
        service_name: Literal["kms"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.KMS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["lambda"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Lambda": ...

    @overload
    def create_client(
        self,
        service_name: Literal["lex-models"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.LexModelBuildingService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["lex-runtime"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.LexRuntimeService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["license-manager"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.LicenseManager": ...

    @overload
    def create_client(
        self,
        service_name: Literal["lightsail"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Lightsail": ...

    @overload
    def create_client(
        self,
        service_name: Literal["machinelearning"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MachineLearning": ...

    @overload
    def create_client(
        self,
        service_name: Literal["macie"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Macie": ...

    @overload
    def create_client(
        self,
        service_name: Literal["managedblockchain"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ManagedBlockchain": ...

    @overload
    def create_client(
        self,
        service_name: Literal["marketplace-entitlement"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MarketplaceEntitlementService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["marketplacecommerceanalytics"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MarketplaceCommerceAnalytics": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mediaconnect"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MediaConnect": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mediaconvert"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MediaConvert": ...

    @overload
    def create_client(
        self,
        service_name: Literal["medialive"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MediaLive": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mediapackage"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MediaPackage": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mediastore"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MediaStore": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mediastore-data"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MediaStoreData": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mediatailor"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MediaTailor": ...

    @overload
    def create_client(
        self,
        service_name: Literal["meteringmarketplace"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MarketplaceMetering": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mgh"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MigrationHub": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mobile"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Mobile": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mq"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MQ": ...

    @overload
    def create_client(
        self,
        service_name: Literal["mturk"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.MTurk": ...

    @overload
    def create_client(
        self,
        service_name: Literal["neptune"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Neptune": ...

    @overload
    def create_client(
        self,
        service_name: Literal["opsworks"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.OpsWorks": ...

    @overload
    def create_client(
        self,
        service_name: Literal["opsworkscm"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.OpsWorksCM": ...

    @overload
    def create_client(
        self,
        service_name: Literal["organizations"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Organizations": ...

    @overload
    def create_client(
        self,
        service_name: Literal["pi"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.PI": ...

    @overload
    def create_client(
        self,
        service_name: Literal["pinpoint"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Pinpoint": ...

    @overload
    def create_client(
        self,
        service_name: Literal["pinpoint-email"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.PinpointEmail": ...

    @overload
    def create_client(
        self,
        service_name: Literal["pinpoint-sms-voice"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.PinpointSMSVoice": ...

    @overload
    def create_client(
        self,
        service_name: Literal["polly"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Polly": ...

    @overload
    def create_client(
        self,
        service_name: Literal["pricing"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Pricing": ...

    @overload
    def create_client(
        self,
        service_name: Literal["quicksight"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.QuickSight": ...

    @overload
    def create_client(
        self,
        service_name: Literal["ram"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.RAM": ...

    @overload
    def create_client(
        self,
        service_name: Literal["rds"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.RDS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["rds-data"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.RDSDataService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["redshift"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Redshift": ...

    @overload
    def create_client(
        self,
        service_name: Literal["rekognition"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Rekognition": ...

    @overload
    def create_client(
        self,
        service_name: Literal["resource-groups"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ResourceGroups": ...

    @overload
    def create_client(
        self,
        service_name: Literal["resourcegroupstaggingapi"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ResourceGroupsTaggingAPI": ...

    @overload
    def create_client(
        self,
        service_name: Literal["robomaker"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.RoboMaker": ...

    @overload
    def create_client(
        self,
        service_name: Literal["route53"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Route53": ...

    @overload
    def create_client(
        self,
        service_name: Literal["route53domains"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Route53Domains": ...

    @overload
    def create_client(
        self,
        service_name: Literal["route53resolver"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Route53Resolver": ...

    @overload
    def create_client(
        self,
        service_name: Literal["s3"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.S3": ...

    @overload
    def create_client(
        self,
        service_name: Literal["s3control"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.S3Control": ...

    @overload
    def create_client(
        self,
        service_name: Literal["sagemaker"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SageMaker": ...

    @overload
    def create_client(
        self,
        service_name: Literal["sagemaker-runtime"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SageMakerRuntime": ...

    @overload
    def create_client(
        self,
        service_name: Literal["sdb"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SimpleDB": ...

    @overload
    def create_client(
        self,
        service_name: Literal["secretsmanager"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SecretsManager": ...

    @overload
    def create_client(
        self,
        service_name: Literal["securityhub"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SecurityHub": ...

    @overload
    def create_client(
        self,
        service_name: Literal["serverlessrepo"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ServerlessApplicationRepository": ...

    @overload
    def create_client(
        self,
        service_name: Literal["servicecatalog"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ServiceCatalog": ...

    @overload
    def create_client(
        self,
        service_name: Literal["servicediscovery"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.ServiceDiscovery": ...

    @overload
    def create_client(
        self,
        service_name: Literal["ses"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SES": ...

    @overload
    def create_client(
        self,
        service_name: Literal["shield"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Shield": ...

    @overload
    def create_client(
        self,
        service_name: Literal["signer"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.signer": ...

    @overload
    def create_client(
        self,
        service_name: Literal["sms"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SMS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["sms-voice"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.PinpointSMSVoice": ...

    @overload
    def create_client(
        self,
        service_name: Literal["snowball"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Snowball": ...

    @overload
    def create_client(
        self,
        service_name: Literal["sns"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SNS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["sqs"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SQS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["ssm"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SSM": ...

    @overload
    def create_client(
        self,
        service_name: Literal["stepfunctions"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SFN": ...

    @overload
    def create_client(
        self,
        service_name: Literal["storagegateway"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.StorageGateway": ...

    @overload
    def create_client(
        self,
        service_name: Literal["sts"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.STS": ...

    @overload
    def create_client(
        self,
        service_name: Literal["support"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Support": ...

    @overload
    def create_client(
        self,
        service_name: Literal["swf"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.SWF": ...

    @overload
    def create_client(
        self,
        service_name: Literal["textract"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Textract": ...

    @overload
    def create_client(
        self,
        service_name: Literal["transcribe"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.TranscribeService": ...

    @overload
    def create_client(
        self,
        service_name: Literal["transfer"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Transfer": ...

    @overload
    def create_client(
        self,
        service_name: Literal["translate"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.Translate": ...

    @overload
    def create_client(
        self,
        service_name: Literal["waf"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.WAF": ...

    @overload
    def create_client(
        self,
        service_name: Literal["waf-regional"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.WAFRegional": ...

    @overload
    def create_client(
        self,
        service_name: Literal["workdocs"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.WorkDocs": ...

    @overload
    def create_client(
        self,
        service_name: Literal["worklink"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.WorkLink": ...

    @overload
    def create_client(
        self,
        service_name: Literal["workmail"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.WorkMail": ...

    @overload
    def create_client(
        self,
        service_name: Literal["workspaces"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.WorkSpaces": ...

    @overload
    def create_client(
        self,
        service_name: Literal["xray"],
        region_name: Optional[str] = ...,
        api_version: Optional[str] = ...,
        use_ssl: bool = ...,
        verify: bool = ...,
        endpoint_url: Optional[str] = ...,
        aws_access_key_id: Optional[str] = ...,
        aws_secret_access_key: Optional[str] = ...,
        aws_session_token: Optional[str] = ...,
        config: Optional[botocore.config.Config] = ...,
    ) -> "botocore.client.XRay": ...
