# udacity-cloud-devops-capstone
./create-stack.sh capstone ../cloudformation/eks-cluster.yml ../cloudformation/eks-cluster-params.json --profile udacity

{
    "StackId": "arn:aws:cloudformation:us-east-1:876162603122:stack/capstone/478fd140-05ae-11ee-bfb4-0eec956bdd8f"
}

./create-stack.sh capstone-eks ../cloudformation/eks-cluster.yml ../cloudformat
ion/eks-cluster-params.json --profile udacity
{
    "StackId": "arn:aws:cloudformation:us-east-1:876162603122:stack/capstone-eks/d0b1ddb0-05ae-11ee-b9e9-12484c5e6641"
}

./create-stack.sh  capstone-node-group ../cloudformation/aws-eks-nodegroup.yml ../cloudformation/amazon-eks-nodegroup-params.json --profile udacity
{
    "StackId": "arn:aws:cloudformation:us-east-1:876162603122:stack/capstone-node-group/0af54650-05b5-11ee-8b49-0af4afb5a211"
}
