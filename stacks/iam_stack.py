from aws_cdk import (
    aws_iam as iam,
    core
)


class IamStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        apply_cdk_stack_permissions = ['cloudformation:CreateChangeSet',
                                       'cloudformation:DeleteChangeSet',
                                       'cloudformation:DeleteStack',
                                       'cloudformation:DescribeChangeSet',
                                       'cloudformation:DescribeStackEvents',
                                       'cloudformation:DescribeStacks',
                                       'cloudformation:ExecuteChangeSet',
                                       'cloudformation:GetTemplate']

        policy_to_create_iam_policies = iam.ManagedPolicy(
            scope=self,
            id="policy_to_create_iam_policies",
            managed_policy_name=f"{core.Aws.STACK_NAME}_policy_to_create_iam_policies"
        )
        policy_to_create_iam_policies.add_statements(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=apply_cdk_stack_permissions+['iam:CreatePolicy',
                                                 'iam:CreatePolicyVersion',
                                                 'iam:DeletePolicy',
                                                 'iam:DeletePolicyVersion',
                                                 'iam:GetPolicy',
                                                 'iam:ListPolicyVersions',
                                                 'sts:GetCallerIdentity'
                                                 ],
            resources=['*'],
        ))

        policy_to_create_pipelines = iam.ManagedPolicy(
            scope=self,
            id="policy_to_create_pipelines",
            managed_policy_name=f"{core.Aws.STACK_NAME}_policy_to_create_pipelines"
        )
        policy_to_create_pipelines.add_statements(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=apply_cdk_stack_permissions+['codebuild:BatchGetProjects',
                                                 'codebuild:CreateProject',
                                                 'codebuild:DeleteProject',
                                                 'codebuild:UpdateProject',
                                                 'codepipeline:CreatePipeline',
                                                 'codepipeline:DeletePipeline',
                                                 'codepipeline:GetPipeline',
                                                 'codepipeline:GetPipelineState',
                                                 'codepipeline:UpdatePipeline',
                                                 'codestar-connections:PassConnection',
                                                 'ecr:CreateRepository',
                                                 'ecr:DeleteRepository',
                                                 'ecr:DescribeRepositories',
                                                 'events:DeleteRule',
                                                 'events:DescribeRule',
                                                 'events:PutRule',
                                                 'events:PutTargets',
                                                 'events:RemoveTargets',
                                                 'iam:CreateRole',
                                                 'iam:DeleteRole',
                                                 'iam:DeleteRolePolicy',
                                                 'iam:GetRole',
                                                 'iam:GetRolePolicy',
                                                 'iam:PassRole',
                                                 'iam:PutRolePolicy',
                                                 'kms:CreateAlias',
                                                 'kms:CreateKey',
                                                 'kms:DescribeKey',
                                                 'kms:GetKeyPolicy',
                                                 'kms:GetKeyRotationStatus',
                                                 'kms:ListResourceTags',
                                                 's3:CreateBucket',
                                                 's3:DeleteBucket',
                                                 's3:DeleteObject',
                                                 's3:ListAllMyBuckets',
                                                 's3:ListBucket',
                                                 's3:PutBucketPublicAccessBlock',
                                                 's3:PutEncryptionConfiguration',
                                                 'sns:CreateTopic',
                                                 'sns:DeleteTopic',
                                                 'sns:GetTopicAttributes',
                                                 'sns:SetTopicAttributes',
                                                 'sns:Subscribe',
                                                 'sns:Unsubscribe',
                                                 ],
            resources=['*'],
        ))
