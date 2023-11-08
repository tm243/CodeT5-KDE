"""
Inference example
"""

from transformers import T5ForConditionalGeneration
from transformers import RobertaTokenizer

tokenizer = RobertaTokenizer.from_pretrained("Salesforce/codet5-base-multi-sum")
model = T5ForConditionalGeneration.from_pretrained('api/saved-pretrained-kde-cpp-tm')

code = """
KdeConnectPlugin::KdeConnectPlugin(QObject *parent, const QVariantList &args)
    : QObject(parent)
    , d(new KdeConnectPluginPrivate)
{
    d->m_device = qvariant_cast<Device *>(args.at(0));
    d->m_pluginName = args.at(1).toString();
    d->m_outgoingCapabilties = args.at(2).toStringList().toSet();
    d->m_config = nullptr;
    d->iconName = args.at(3).toString();
}
"""

input_ids = tokenizer(code, return_tensors='pt').input_ids
outputs = model.generate(input_ids, max_new_tokens=300)

print("Result:", tokenizer.decode(outputs[0], skip_special_tokens=True))

