Vagrant. configure ("2") do |config|
    config.vm.box = "dummy"
    ###For ANS credentiale###
    aws_access_key=""
    aws_secret_key=""
    aws_keypair_name=""
    aws_private_key_path=""
    config.vm-provider :aws do |aws, override|
      aws.acces_key_id=aws_access_key
      aws.secret_access_key=aws_secret_key
      awa.keypair_name=aws_keypair_name
      override.ssh.private_key_path=aws_private_key_path
      aws.region="us-east-1" $ Change to your desired region
      aws.instance_type="t3.micro"
      aws.security_groups=["sg-09ff8c2894b55f951"]
      aws.ami="ami-" Replace with a suitable AMI, like Ubuntu
    end
    config.vm.define "child-1" do |web|
      web.vm.hostname = "child-1"
      web.vm.network :private_network, type: "dhcp"
    end
    config.vm.define "child-2" do | db|
      db.vm.hostname = "child-2"
      db.vm.network :private_network, type: "dhcp"
    end
end

