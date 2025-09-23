using EC2 key pair "eks-ssh-key"
node "ip-10-0-1-75.ec2.internal" is ready
node "ip-10-0-6-38.ec2.internal" is ready
Host: <public-ip-of-node>
Username: ec2-user
Private key: eks-ssh-key.ppk
ssh -i eks-ssh-key.pem ec2-user@54.82.86.100
mv ~/Downloads/eks-ssh-key.pem ./
cd ~/Downloads
eks-ssh-key.pem
chmod 400 ~/Downloads/eks-ssh-key.pem
ssh -i ~/Downloads/eks-ssh-key.pem ec2-user@54.82.86.100
aws ec2 describe-instances --region us-east-1 --query "Reservations[*].Instances[*].[InstanceId,PublicIpAddress,State.Name]" --output table
sudo yum install git -y 
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Lalithya15/devops-intern.git
git branch -M main
git push -u origin main
