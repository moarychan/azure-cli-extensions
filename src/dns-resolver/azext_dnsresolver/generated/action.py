# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# pylint: disable=protected-access

# pylint: disable=no-self-use


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddIpConfigurations(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddIpConfigurations, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'private-ip-address':
                d['private_ip_address'] = v[0]

            elif kl == 'private-ip-allocation-method':
                d['private_ip_allocation_method'] = v[0]

            elif kl == 'id':
                sub_d = d
                if 'subnet' not in sub_d:
                    sub_d['subnet'] = {}
                sub_d = sub_d['subnet']

                sub_d['id'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter ip-configurations. All possible keys are:'
                    ' private-ip-address, private-ip-allocation-method, id'.format(k)
                )

        return d


class AddDnsResolverOutboundEndpoints(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDnsResolverOutboundEndpoints, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'id':
                d['id'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter dns-resolver-outbound-endpoints. All possible keys'
                    ' are: id'.format(k)
                )

        return d


class AddDnsResolverForwardingRuleUpdateTargetDnsServers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDnsResolverForwardingRuleUpdateTargetDnsServers, self).__call__(
            parser, namespace, action, option_string
        )

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'ip-address':
                d['ip_address'] = v[0]

            elif kl == 'port':
                d['port'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter target-dns-servers. All possible keys are:'
                    ' ip-address, port'.format(k)
                )

        return d


class AddDnsResolverForwardingRuleUpdateMetadata(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.metadata = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            v = properties[k]

            d[k] = v[0]

        return d


class AddDnsResolverForwardingRuleCreateTargetDnsServers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDnsResolverForwardingRuleCreateTargetDnsServers, self).__call__(
            parser, namespace, action, option_string
        )

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'ip-address':
                d['ip_address'] = v[0]

            elif kl == 'port':
                d['port'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter target-dns-servers. All possible keys are:'
                    ' ip-address, port'.format(k)
                )

        return d


class AddDnsResolverForwardingRuleCreateMetadata(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.metadata = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            v = properties[k]

            d[k] = v[0]

        return d


class AddDnsResolverVnetLinkUpdateMetadata(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.metadata = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            v = properties[k]

            d[k] = v[0]

        return d


class AddDnsResolverVnetLinkCreateMetadata(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.metadata = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            v = properties[k]

            d[k] = v[0]

        return d