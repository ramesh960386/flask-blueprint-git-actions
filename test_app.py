from app import index


def test_index():
    assert index() == 'Hello world!'



# https://medium.com/innovation-incubator/deploying-code-from-github-to-aws-ec2-with-codepipeline-4639e8fbba28
# https://afourtech.com/complete-guide-to-deploying-github-project-on-amazon-ec2-using-aws-codedeploy-service-and-github-actions/
# https://dev.to/ankushbehera/a-complete-guide-to-deploy-github-project-on-amazon-ec2-using-github-actions-and-aws-codedeploy-3f0b
# https://devopscube.com/checkout-clone-specific-git-commit-id-sha/